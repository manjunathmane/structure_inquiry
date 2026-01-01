import sys

def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3

def get_student_details():
    if len(sys.argv) != 5:
        print("Usage: python app.py <student_name> <m1> <m2> <m3>")
        sys.exit(1)

    name = sys.argv[1]
    m1 = float(sys.argv[2])
    m2 = float(sys.argv[3])
    m3 = float(sys.argv[4])

    avg = calculate_average(m1, m2, m3)

    return {
        "name": name,
        "m1": m1,
        "m2": m2,
        "m3": m3,
        "average": avg
    }

def display_student(student):
    print("Student Result")
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