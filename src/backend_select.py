"""Backend discovery helpers for IBM Runtime smoke tests.

This module intentionally avoids hardcoded backend names and supports:
- Environment-based credentials (API_KEY + INSTANCE)
- Existing saved local account (QiskitRuntimeService default init)
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any, Iterable, List


class MissingCredentialsError(RuntimeError):
    """Raised when Runtime credentials are unavailable or invalid."""


class BackendSelectionError(RuntimeError):
    """Raised when no suitable backend can be selected."""


@dataclass(frozen=True)
class RuntimeConfig:
    """Configuration values used to initialize ``QiskitRuntimeService``."""

    channel: str = "ibm_quantum_platform"
    token: str | None = None
    instance: str | None = None

    @classmethod
    def from_env(cls) -> "RuntimeConfig":
        """Build config from environment variables.

        Recognized variables:
        - QISKIT_IBM_TOKEN (preferred), API_KEY, or IBM_QUANTUM_API_KEY
        - QISKIT_IBM_INSTANCE (preferred), INSTANCE, or IBM_QUANTUM_INSTANCE
        - QISKIT_IBM_CHANNEL (preferred) or CHANNEL
          (optional, defaults to ibm_quantum_platform)
        """

        token = os.getenv("QISKIT_IBM_TOKEN") or os.getenv("API_KEY") or os.getenv("IBM_QUANTUM_API_KEY")
        instance = os.getenv("QISKIT_IBM_INSTANCE") or os.getenv("INSTANCE") or os.getenv("IBM_QUANTUM_INSTANCE")
        channel = os.getenv("QISKIT_IBM_CHANNEL") or os.getenv("CHANNEL") or "ibm_quantum_platform"
        return cls(channel=channel, token=token, instance=instance)


def _clean(value: str | None) -> str | None:
    if value is None:
        return None
    value = value.strip()
    return value or None


def _is_placeholder(value: str | None) -> bool:
    if not value:
        return False
    upper = value.upper()
    return upper.startswith("YOUR_") or upper.endswith("_HERE")


def _runtime_service_class() -> Any:
    try:
        from qiskit_ibm_runtime import QiskitRuntimeService  # pylint: disable=import-outside-toplevel
    except Exception as exc:  # noqa: BLE001
        raise MissingCredentialsError(
            "qiskit-ibm-runtime is not installed. Install it to run the IBM Runtime smoke test."
        ) from exc
    return QiskitRuntimeService


def initialize_service(config: RuntimeConfig | None = None) -> Any:
    """Initialize Runtime service safely.

    Precedence:
    1) If environment credentials are present and non-placeholder, use them.
    2) Otherwise try existing saved account with ``QiskitRuntimeService()``.
    """

    cfg = config or RuntimeConfig.from_env()
    token = _clean(cfg.token)
    instance = _clean(cfg.instance)

    has_env_credentials = bool(token and instance)
    env_credentials_usable = has_env_credentials and not (_is_placeholder(token) or _is_placeholder(instance))

    runtime_service_cls = _runtime_service_class()

    if env_credentials_usable:
        try:
            return runtime_service_cls(channel=cfg.channel, token=token, instance=instance)
        except Exception as exc:  # noqa: BLE001
            raise MissingCredentialsError(
                "Could not initialize IBM Runtime from environment credentials. "
                "Check QISKIT_IBM_TOKEN/QISKIT_IBM_INSTANCE values in .env."
            ) from exc

    try:
        return runtime_service_cls()
    except Exception as exc:  # noqa: BLE001
        raise MissingCredentialsError(
            "No usable IBM Runtime credentials found. Set QISKIT_IBM_TOKEN and "
            "QISKIT_IBM_INSTANCE in .env, "
            "or save an account locally. For no-account testing, run "
            "notebooks/00_local_statevector_smoke.ipynb and notebooks/01_local_aer_smoke.ipynb."
        ) from exc


def list_candidate_backends(service: Any, min_num_qubits: int = 5) -> List[object]:
    """Return available non-simulator operational backends."""

    return list(
        service.backends(
            simulator=False,
            operational=True,
            min_num_qubits=min_num_qubits,
        )
    )


def select_least_busy_backend(service: Any, min_num_qubits: int = 5) -> object:
    """Select a backend using IBM Runtime least-busy logic."""

    candidates = list_candidate_backends(service=service, min_num_qubits=min_num_qubits)
    if not candidates:
        raise BackendSelectionError(
            "No operational hardware backends found for the requested filters "
            f"(simulator=False, operational=True, min_num_qubits={min_num_qubits})."
        )

    try:
        return service.least_busy(
            simulator=False,
            operational=True,
            min_num_qubits=min_num_qubits,
        )
    except Exception as exc:  # noqa: BLE001
        raise BackendSelectionError("Failed to select least-busy backend from candidates.") from exc


def summarize_backends(backends: Iterable[object], limit: int = 10) -> List[str]:
    """Create readable backend summary lines for notebook output."""

    lines: List[str] = []
    for backend in list(backends)[:limit]:
        name = getattr(backend, "name", str(backend))
        qubits = getattr(backend, "num_qubits", "?")
        pending = "?"
        try:
            status_fn = getattr(backend, "status", None)
            if callable(status_fn):
                status = status_fn()
                pending = getattr(status, "pending_jobs", "?")
        except Exception:  # noqa: BLE001
            pass
        lines.append(f"{name} | qubits={qubits} | pending_jobs={pending}")
    return lines
