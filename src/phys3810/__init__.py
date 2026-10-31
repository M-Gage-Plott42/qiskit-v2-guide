"""Small, explicitly scoped quantum-circuit implementations for PHYS 3810."""

from .grover import diffusion_operator, grover_circuit, grover_iteration, phase_oracle
from .hhl import hhl_circuit, hhl_reciprocal_rotation
from .qft import qft_circuit
from .qpe import qpe_circuit

__all__ = [
    "phase_oracle", "diffusion_operator", "grover_iteration", "grover_circuit",
    "qft_circuit", "qpe_circuit", "hhl_circuit", "hhl_reciprocal_rotation",
]
