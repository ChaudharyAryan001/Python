
print("Collection Manipulator\n")

print("welcome to student data organizer..")
student_list=[]

while True:
    print("\nSelect Any one : ")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Unique Subjects Offered")
    print("6. Exit")

    select=input("\nSelect any option : ")

    if select=="1" or select=="01":
        print("\nAdd New Student")
        id=input("enter the student id : ")
        name=input("Enter your name : ")
        age=int(input("Enter the age : "))
        dob=input("Enter the Date of Birth : ")
        grade=input("Enter the grade : ")        
        subject=input("Enter the subject name : ")
        subject_list = [s.strip() for s in subject.split(",")]
        
        
        tple=(id,dob)

        info={
            "id_info": tple, 
            "name": name, 
            "age": age, 
            "grade": grade, 
            "subjects": subject_list
        }

        student_list.append(info)
        print("student added successfully")

    elif select=="2" or select=="02":
        print("\nDisplay All Students")

        for student in student_list:
            s_id=student["id_info"][0]
            subj_str=", ".join(student["subjects"])

            print(f"Student ID: {s_id} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']} | Subjects: {subj_str}")

    elif select=="3" or select=="03":
        edit=input("\nupdate student Id Given :  ")
        
       
        for student in student_list:
            if edit==student["id_info"][0]:
        
                print(f"\nStudent Name : {student['name']}")

                new_age=int(input("Enter The New Age : "))
                student["age"]=new_age

                new_subjects=input("Enter The Subject : ")
                student["subjects"]=[s.strip()   for s in new_subjects.split(",")]

                print("\ninformation Update Successfully : ")
                break

    elif select=="4" or select=="04":
        delete_id=input("\nenter student ID to delete : ")
        found = False
        
        for i in range(len(student_list)):
            if delete_id==student_list[i]["id_info"][0]:
                del student_list[i]
                print("\nRecord delete successfully")
                found = True
                break

    elif select=="5" or select=="05":
        print("\nUnique subject offered")
        unique_subject=set() 

        for student in student_list:
            unique_subject.update(student["subjects"])

        if unique_subject:
            print("\nAvailable Subjects: ", ", ".join(unique_subject))
        else:
            print("\nNo subjects found.")       

    elif select=="6" or select=="06":
        print("\nThank you for using the Student Data Organizer!")
        break
