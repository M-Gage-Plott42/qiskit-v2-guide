"""Small, explicitly scoped quantum-circuit implementations for PHYS 3810."""

from .grover import diffusion_operator, grover_circuit, grover_iteration, phase_oracle

__all__ = ["phase_oracle", "diffusion_operator", "grover_iteration", "grover_circuit"]
