def main():
    # Prompt the user for input
    fahrenheit = input("Enter temperature in Fahrenheit: ")
    
    # Convert input to float
    fahrenheit = float(fahrenheit)

    # Apply conversion formula
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Display result
    print(f"Temperature: {fahrenheit}F = {celsius}C")

main()
