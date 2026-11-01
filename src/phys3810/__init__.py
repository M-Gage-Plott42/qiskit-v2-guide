"""Small, explicitly scoped quantum-circuit implementations for PHYS 3810."""

from .grover import diffusion_operator, grover_circuit, grover_iteration, phase_oracle
from .hhl import hhl_circuit, hhl_reciprocal_rotation
from .qft import qft_circuit
from .qpe import qpe_circuit
from .shor import (
    classical_factor_15, factors_from_order_15, modular_multiplier_15,
    order_finding_15, recover_order_15,
)

__all__ = [
    "phase_oracle", "diffusion_operator", "grover_iteration", "grover_circuit",
    "qft_circuit", "qpe_circuit", "hhl_circuit", "hhl_reciprocal_rotation",
    "modular_multiplier_15", "order_finding_15", "recover_order_15",
    "factors_from_order_15", "classical_factor_15",
]
