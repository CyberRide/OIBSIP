# Function to calculate BMI based on weight and height
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Function to classify BMI into health categories
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Main program execution
def main():
    try:
        # Prompt user for weight and height input
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    except ValueError:
        # Handle invalid input (non-numeric values)
        print("Invalid input. Please enter numeric values for weight and height.")
        return

    # Validate positive values for weight and height
    if weight <= 0 or height <= 0:
        print("Weight and height must be positive values.")
        return

    # Calculate BMI and classify into categories
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    # Display the calculated BMI and health category to the user
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

# Run the main program if this script is executed directly
if __name__ == "__main__":
    main()
