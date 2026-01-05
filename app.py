def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3

def get_student_details():
    name = input("Enter student name: ")

    try:
        m1 = float(input("Enter marks 1: "))
        m2 = float(input("Enter marks 2: "))
        m3 = float(input("Enter marks 3: "))
    except ValueError:
        print("Marks must be numeric values")
        return None

    avg = calculate_average(m1, m2, m3)

    return {
        "name": name,
        "m1": m1,
        "m2": m2,
        "m3": m3,
        "average": avg
    }

def display_student(student):
    if student is None:
        return

    print("\nStudent Result")
    print("----------------")
    print("Name:", student["name"])
    print("Marks:", student["m1"], student["m2"], student["m3"])
    print("Average:", student["average"])

    if student["average"] >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")

if __name__ == "__main__":
    student = get_student_details()
    display_student(student)
