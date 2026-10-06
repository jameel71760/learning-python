students = []

while True:
    print("==== STUDENT MANAGEMENT =====")
    print("1. Add student")
    print("2. View student")
    print("3. Search student")
    print("4. Remove student")
    print("5. Exit")

    choice = input("Select your choice")

    if choice =="1":
        name = input("What is your name?")
        age = int(input("How old are you?"))

        student = {
            "name": name,
            "age": age
        }

        students.append(student)

        print("Student Added Successfully")
        print("Name:", name)
        print("Age:", age)

    elif choice =="2":
        for student in students:
            print("Name", student["name"])
            print("Age", student["age"])

    elif choice == "3":      
        search_name = input("Enter student name to search" )

        found = False

        for student in students:
            if student["name"] == search_name:
                print("Student found!")
                print("Name:", student["name"])
                print("Age:", student["age"])

                found = True
                break

        if found== False:
            print("student not found.")


    elif choice=="4":
        remove_name = input("Enter student name to remove: ")

        found = False

        for student in students:
            if student["name"] == remove_name:
                students.remove(student)
                print("remove student successfully!")
                found = True
                break
            
            if found == False:
                print("Student not found")


    elif choice=="5":
        print("Exit")
        break