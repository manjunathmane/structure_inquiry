from daily_calorie import calculate_daily_calories, calorie_status

def test_calorie_calculation():
    age = 20
    weight = 60
    assert calculate_daily_calories(age, weight) == (60 * 24 - 20 * 3)

def test_invalid_values():
    assert calculate_daily_calories(0, 50) == 0
    assert calculate_daily_calories(20, 0) == 0

def test_high_calorie_status():
    assert calorie_status(2600) == "High Calorie Requirement"

def test_moderate_calorie_status():
    assert calorie_status(2000) == "Moderate Calorie Requirement"

def test_low_calorie_status():
    assert calorie_status(1500) == "Low Calorie Requirement"
