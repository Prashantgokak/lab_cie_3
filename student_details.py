def test_student_details(usn, name, div, age):
    return {
        "student_usn": (usn),
        "student_name": name,
        "student_div": div,
        "student_age": (age)
    }


if __name__ == "__main__":
    usn ="302"
    name ="akash"
    div ="E"
    age="19" 
    print(test_student_details(302, "akash", "E", 19))
