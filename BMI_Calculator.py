# BMI Calculator in Python

def calculate_bmi(weight, height):
    """Calculate and return the Body Mass Index (BMI)."""
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    """Return the BMI category based on the BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    # User input for weight and height
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in meters (m): "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    # Determine the BMI category
    category = bmi_category(bmi)

    # Display the results
    print(f"Your BMI is: {bmi:.2f}")
    print(f"This is considered: {category}")

if __name__ == "__main__":
    main()
