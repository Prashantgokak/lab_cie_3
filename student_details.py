def test_student_details(usn, name, div, age):
    return {
        "student_usn": str(usn),
        "student_name": name,
        "student_div": div,
        "student_age": str(age)
    }


if __name__ == "__main__":
    print(test_student_details(302, "akash", "E", 19))
