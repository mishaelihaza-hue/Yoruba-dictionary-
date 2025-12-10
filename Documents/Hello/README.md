# Physics Formulas Utility

This small Python package provides functions for common physics formulas:

- Displacement: `S = u*t + 1/2*g*t^2`
- Impulse: `I = m*(v - u)`
- Gravitational force: `F = G*M*m / r^2`
- Kinematic relation: `V^2 = u^2 - 2*g*H`
- Ohm's law: `V = I*R`

Files:
- `physics.py` — library functions for each formula
- `run_physics.py` — simple CLI to compute the formulas

Quick examples (run in PowerShell):

```powershell
python run_physics.py displacement --u 5 --t 2
python run_physics.py impulse --m 2 --u 3 --v 8
python run_physics.py gravity --M 5.97e24 --m 1000 --r 6.371e6
python run_physics.py v_squared --u 10 --g 9.81 --H 5
python run_physics.py ohm --I 0.5 --R 10
```

Examples using `physics.py` directly:

```python
from physics import displacement, impulse

print(displacement(5, 2))
print(impulse(2, 8, 3))
```

Default gravity uses `g = 9.81 m/s^2` and the gravitational constant `G = 6.67430e-11`.

