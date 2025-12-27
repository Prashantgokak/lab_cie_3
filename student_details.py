def student_details(usn, name,div,age):
    result= (
        student USN ="{usn}";
        student NAME ="{name}";
        student DIVION ="{div}";
        student AGE ="{age}";
    )
    return result 
if __name__ == "__main__":
 print(student_details(302,"akash","E",19))

