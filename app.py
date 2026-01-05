import sys

def calculate_daily_calories(age, weight):
    """
    Calculate daily calorie requirement based on age and weight
    (Simple logic for academic/demo purpose)
    """
    if age <= 0 or weight <= 0:
        return 0

    # Simple formula (example logic)
    return (weight * 24) - (age * 3)


def calorie_status(calories):
    if calories >= 2500:
        return "High Calorie Requirement"
    elif calories >= 1800:
        return "Moderate Calorie Requirement"
    else:
        return "Low Calorie Requirement"


if __name__ == "__main__":

    script_name = sys.argv[0]

    if len(sys.argv) == 4:
        person_name = sys.argv[1]
        age = int(sys.argv[2])
        weight = int(sys.argv[3])
        print("User provided calorie details:")
    else:
        person_name = "Shreya"
        age = 21
        weight = 55
        print("No input given - using default values:")

    daily_calories = calculate_daily_calories(age, weight)
    status = calorie_status(daily_calories)

    print("\n========== Daily Calorie Requirement ==========")
    print("Script Name:", script_name)
    print("Name:", person_name)
    print("Age:", age)
    print("Weight:", weight, "kg")
    print("Daily Calories Needed:", daily_calories)
    print("Calorie Status:", status)
