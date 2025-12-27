def student_details(usn, name, div, age):
    result = (
        f"Student USN = {usn}\n"
        f"Student Name = {name}\n"
        f"Student Division = {div}\n"
        f"Student Age = {age}"
    )
    return result

if __name__ == "__main__":
    print(student_details(302, "akash", "E", 19))
