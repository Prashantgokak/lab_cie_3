from student_details import test_student_details

expected_output = {
    "student_usn": "302",
    "student_name": "akash",
    "student_div": "E",
    "student_age": "19"
}

assert test_student_details(302, "akash", "E", 19) == expected_output
