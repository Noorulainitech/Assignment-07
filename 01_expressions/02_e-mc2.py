def main():
    # Speed of light constant (m/s)
    C = 299792458

    # Prompt user for mass
    mass = float(input("Enter kilos of mass: "))

    print("\ne = m * C^2...\n")
    print(f"m = {mass} kg")
    print(f"C = {C} m/s\n")

    # Calculate energy
    energy = mass * C ** 2

    # Print result
    print(f"{energy} joules of energy!")

main()
