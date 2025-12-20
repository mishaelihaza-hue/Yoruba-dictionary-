"""Usage examples:
  python run_physics.py displacement --u 5 --t 2
  python run_physics.py impulse --m 2 --u 3 --v 8
  python run_physics.py gravity --M 5.97e24 --m 1000 --r 6.371e6
  python run_physics.py v_squared --u 10 --g 9.81 --H 5
  python run_physics.py ohm --I 0.5 --R 10
"""
from __future__ import annotations

import argparse
import sys
from physics import displacement, impulse, gravitational_force, v_squared, ohms_law, main as interactive_main


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Compute common physics formulas.")
    sub = p.add_subparsers(dest="cmd", required=True)

    sd = sub.add_parser("displacement", help="S = u*t + 1/2*g*t^2")
    sd.add_argument("--u", type=float, required=True, help="initial velocity (m/s)")
    sd.add_argument("--t", type=float, required=True, help="time (s)")
    sd.add_argument("--g", type=float, default=9.81, help="gravity (m/s^2)")

    si = sub.add_parser("impulse", help="I = m*(v - u)")
    si.add_argument("--m", type=float, required=True, help="mass (kg)")
    si.add_argument("--u", type=float, required=True, help="initial velocity (m/s)")
    si.add_argument("--v", type=float, required=True, help="final velocity (m/s)")

    sg = sub.add_parser("gravity", help="F = G*M*m / r^2")
    sg.add_argument("--M", type=float, required=True, help="mass 1 (kg)")
    sg.add_argument("--m", type=float, required=True, help="mass 2 (kg)")
    sg.add_argument("--r", type=float, required=True, help="distance (m)")
    sg.add_argument("--G", type=float, default=6.67430e-11, help="gravitational constant")

    sv = sub.add_parser("v_squared", help="V^2 = u^2 - 2*g*H")
    sv.add_argument("--u", type=float, required=True, help="initial velocity (m/s)")
    sv.add_argument("--g", type=float, required=True, help="acceleration (m/s^2)")
    sv.add_argument("--H", type=float, required=True, help="height/displacement (m)")

    so = sub.add_parser("ohm", help="V = I * R")
    so.add_argument("--I", type=float, required=True, help="current (A)")
    so.add_argument("--R", type=float, required=True, help="resistance (Ω)")

    return p.parse_args()


def main() -> None:
    # If no command-line arguments are provided, launch the interactive prompt
    if len(sys.argv) == 1:
        interactive_main()
        return

    args = parse_args()
    if args.cmd == "displacement":
        result = displacement(args.u, args.t, args.g)
        print(f"Displacement S = {result}")
    elif args.cmd == "impulse":
        result = impulse(args.m, args.v, args.u)
        print(f"Impulse I = {result}")
    elif args.cmd == "gravity":
        result = gravitational_force(args.M, args.m, args.r, args.G)
        print(f"Gravitational force F = {result} N")
    elif args.cmd == "v_squared":
        result = v_squared(args.u, args.g, args.H)
        print(f"V^2 = {result}")
    elif args.cmd == "ohm":
        result = ohms_law(args.I, args.R)
        print(f"Voltage V = {result} V")


if __name__ == "__main__":
    main()
