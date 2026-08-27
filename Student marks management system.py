student_name=[]
student_marks=[]

while True:
    print("="*40)
    print("STUDENT MARKS MANAGEMENT SYSTEM")
    print("="*40)
    print("1. Insert Student Record")
    print("2. Delete Student Record")
    print("3. Update Student Marks")
    print("4. Traverse / Display All Record")
    print("5. Search Student")
    print("6. Show Statistics")
    print("7. Exit")

    choice=input("Enter Your choice(1-7): ").strip()

    if choice =='1':
        name=input("Enter student name: ").strip()

        if name in student_name:
            print(f"Student '{name}' already exists! Use update option instead.\n")
        else:
            marks=float(input(f"Enter Marks for {name}: "))
            student_name.append(name)
            student_marks.append(marks)
            print(f"Record for '{name}' instead successfully.\n")

    elif choice=='2':
        name=input("Enter student name to delete: ").strip()

        if name in student_name:
            index=student_name.index(name)
            student_name.pop(index)
            student_marks.pop(index)
            print(f"Record for '{name}' deleted successfully.\n")
        else:
            print(f"Student '{name}' not found.\n")

    elif choice=='3':
            name=input("Enter student name to update: ").strip()
    
            if name in student_name:
                index=student_name.index(name)
                new_marks=float(input(f"Enter new marks for {name}: "))
                student_marks[index]=new_marks
                print(f"Marks for '{name}' update successfully.\n")
            else:
                print(f"Student '{name}' not found.\n")

    elif choice=='4':
    
        if len(student_name)==0:
            print("No Records to display.\n")
        else:
            print("\n {:<45} {:<20} {:<10}".format("No.", "name", "Marks"))
            print("-"*35)
            for i in range(len(student_name)):
                print("{:<5} {:<20} {:<10}".format(i+1,student_name[i],student_marks[i]))
            print()

    elif choice=='5':
        name=input("Enter Student name to Search: ").strip()

        if name in student_name:
            index=student_name.index(name)
            print(f"{name} -> marks: {student_marks[index]}\n")
        else:
            print(f"Student '{name}' not found.\n")

    elif choice=='6':
        if len(student_marks)==0:
            print("No Records available for statistics.\n")
        else:
            total=sum(student_marks)
            average=total/len(student_marks)
            highest=max(student_marks)
            lowest=min(student_marks)

            topper_index=student_marks.index(highest)
            weakest_index=student_marks.index(lowest)

            print("\n========== Class Statistics ==========")
            print(f"Total Students:{len(student_name)}")
            print(f"Average Marks:{average:.2f}")
            print(f"Highest Marks:{highest} (Student: {student_name[topper_index]})")
            print(f"Lowest Marks:{lowest} (Student: {student_name[weakest_index]})")
            print()

    elif choice=='7':
        print("Existing Program. Thank You!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.\n")