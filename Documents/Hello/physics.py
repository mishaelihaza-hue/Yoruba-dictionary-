"""Very simple physics formulas for beginners.

Each function implements one formula with straightforward arguments.
"""


def displacement(u, t, g=9.81):
    """Return S = u*t + 1/2*g*t^2"""
    return u * t + 0.5 * g * t * t


def impulse(m, v, u):
    """Return I = m*(v - u)"""
    return m * (v - u)


def gravitational_force(G, M, m, r):
    """Return F = G*M*m / r^2"""
    return G * M * m / (r * r)


def v_squared(u, g, H):
    """Return V^2 = u^2 - 2*g*H"""
    return u * u - 2 * g * H


def ohms_law(I, R):
    """Return V = I * R"""
    return I * R


def _prompt_float(prompt, default=None):
    """Prompt until a valid float is entered. If default is given, Enter accepts it.

    Returns a float.
    """
    while True:
        if default is None:
            raw = input(f"{prompt}: ")
            if raw.strip() == "":
                print("Please enter a number.")
                continue
        else:
            raw = input(f"{prompt} (default {default}): ")
            if raw.strip() == "":
                try:
                    return float(default)
                except ValueError:
                    print("Default value is not a valid number.")
                    continue
        try:
            return float(raw)
        except ValueError:
            print("Invalid number. Try again.")


def main():
    print("Choose a formula by number:")
    print("1) displacement: S = u*t + 1/2*g*t^2")
    print("2) impulse: I = m*(v - u)")
    print("3) gravity: F = G*M*m / r^2")
    print("4) v_squared: V^2 = u^2 - 2*g*H")
    print("5) ohm: V = I * R")
    choice = input("Enter 1-5: ")
    if choice == "1":
        u = _prompt_float("Enter u")
        t = _prompt_float("Enter t")
        g = _prompt_float("Enter g", default=9.81)
        print("S =", displacement(u, t, g))
    elif choice == "2":
        m = _prompt_float("Enter m")
        v = _prompt_float("Enter v")
        u = _prompt_float("Enter u")
        print("I =", impulse(m, v, u))
    elif choice == "3":
        G = _prompt_float("Enter G", default=6.67430e-11)
        M = _prompt_float("Enter M")
        m = _prompt_float("Enter m")
        r = _prompt_float("Enter r")
        print("F =", gravitational_force(G, M, m, r))
    elif choice == "4":
        u = _prompt_float("Enter u")
        g = _prompt_float("Enter g", default=9.81)
        H = _prompt_float("Enter H")
        print("V^2 =", v_squared(u, g, H))
    elif choice == "5":
        I = _prompt_float("Enter I")
        R = _prompt_float("Enter R")
        print("V =", ohms_law(I, R))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
