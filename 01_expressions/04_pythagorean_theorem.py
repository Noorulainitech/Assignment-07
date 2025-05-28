import math

def main():
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Apply Pythagorean theorem: hypotenuse = sqrt(ab² + ac²)
    bc = math.sqrt(ab ** 2 + ac ** 2)

    print(f"The length of BC (the hypotenuse) is: {bc}")

main()
