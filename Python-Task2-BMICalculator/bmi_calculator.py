# Project: BMI Calculator (OIBSIP - Python Programming Task 2)
# Author: Apeksha Suhas Phapale

def compute_bmi(weight_kg, height_m):
    """Calculates Body Mass Index using weight in kg and height in meters."""
    return weight_kg / (height_m ** 2)

def evaluate_health_status(bmi_score):
    """Determines the BMI category and provides a brief wellness note."""
    if bmi_score < 18.5:
        return "Underweight", "Consider a balanced, nutrient-rich diet."
    elif 18.5 <= bmi_score <= 24.9:
        return "Normal weight", "Great job! Maintain your healthy lifestyle."
    elif 25.0 <= bmi_score <= 29.9:
        return "Overweight", "Regular exercise and mindful eating can help."
    else:
        return "Obese", "Consult a healthcare professional for personalized guidance."

def run_bmi_app():
    print("\n" + "*" * 42)
    print("      PYTHON BMI CALCULATOR - APEKSHA     ")
    print("*" * 42)
    
    while True:
        try:
            weight_kg = float(input("\nEnter your weight (in kg): "))
            height_m = float(input("Enter your height (in meters): "))
            
            if weight_kg <= 0 or height_m <= 0:
                print("Error: Values must be greater than zero. Try again.")
                continue
                
            bmi_score = compute_bmi(weight_kg, height_m)
            status, advice = evaluate_health_status(bmi_score)
            
            print("\n---------------- SUMMARY -----------------")
            print(f"Calculated BMI : {bmi_score:.2f}")
            print(f"Health Status  : {status}")
            print(f"Wellness Note  : {advice}")
            print("------------------------------------------")
            
        except ValueError:
            print("Invalid entry! Please type numeric values only (e.g., 58.5 or 1.65).")
            continue
            
        again = input("\nCheck another BMI? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThank you for using Apeksha's BMI Calculator. Goodbye!")
            break

if __name__ == "__main__":
    run_bmi_app()
