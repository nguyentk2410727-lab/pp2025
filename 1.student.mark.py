students = []
courses = []
marks = {}

def input_students():
    n = int(input("Enter number of students: "))
    for _ in range(n):
        sid = input("Enter student ID: ")
        name = (input("Enter student name: "))
        dob = input("Enter student date of birth (DD/MM/YYYY): ")
        students.append({'id': sid, 'name': name, 'dob': dob})

def input_courses():
    n = int(input("Enter number of courses: "))
    for _ in range(n):
        cid = input("Enter course ID: ")
        name = input("Enter course name: ") 
        courses.append({'id': cid, 'name': name})

def input_marks():
    sid = input("Student ID: ")
    cid = input("Course ID: ")
    score = float(input("Mark: "))
    marks[(sid, cid)] = score

def list_students():
    for s in students:
        print(s["id"], s["name"], s["dob"])

def list_courses():
    for c in courses:
        print(c["id"], c["name"])

def show_marks():
    cid = input("Course ID: ")
    for(sid, course_id), score in marks.items():
        if course_id == cid:
            print("Student ID:", sid, "Mark:", score)

def menu():
    while True:
        print("\nMenu:")
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. List Students")
        print("5. List Courses")
        print("6. Show Marks by Course")
        print("0. Exit")

        choice = input("Choose: ")
        
        if choice == '1':
            input_students()
        elif choice == '2':
            input_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif choice == '6':
            show_marks()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

menu()