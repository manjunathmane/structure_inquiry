from app import register_courses

def test_course_registration():
    student_name ="Alice"
    courses = [
        {"course_name":"Python","credits":4},
        {"course_name":"DevOps","credits":3}
    ]

    result = register_courses(student_name, courses)

    assert result["student_name"] =="Alice"
    assert len(result["courses"]) ==2
