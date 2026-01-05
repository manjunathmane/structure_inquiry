import sys

def register_courses(student_name, courses):
    return {
        "student_name": student_name,
        "courses": courses
    }

def get_course_details():
    if len(sys.argv) < 4 or len(sys.argv) % 2 != 0:
        print("Invalid arguments.")
        print("Usage: python app.py <student_name> <course1> <credits1> <course2> <credits2> ...")
        return None   # Do NOT exit with error code

    student_name = sys.argv[1]
    courses = []
    args = sys.argv[2:]

    for i in range(0, len(args), 2):
        try:
            courses.append({
                "course_name": args[i],
                "credits": int(args[i + 1])
            })
        except ValueError:
            print("Credits must be numeric.")
            return None

    return register_courses(student_name, courses)

def display_courses(data):
    if not data:
        return

    print("Course Registration Details")
    print("Student Name:", data["student_name"])

    for course in data["courses"]:
        print(f"Course: {course['course_name']} | Credits: {course['credits']}")

if __name__ == "__main__":
    registration = get_course_details()
    display_courses(registration)
