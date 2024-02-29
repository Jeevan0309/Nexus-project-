class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

class Teacher(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

class Head(Person):
    def __init__(self, name, age, username, password):
        super().__init__(name, age)
        self.username = username
        self.password = password

class StudentDatabase:
    def __init__(self):
        self.students = {}
        self.teachers = {}  # Dictionary to store teacher details

    def add_student(self, student):
        self.students[student.roll_no] = student

    def add_teacher(self, teacher):
        self.teachers[teacher.employee_id] = teacher

    def display_student_details(self, roll_no):
        student = self.students.get(roll_no)
        if student:
            print(f"Roll No: {student.roll_no}")
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
        else:
            print(f"Student with Roll No {roll_no} not found.")

    def display_teacher_details(self, employee_id):
        teacher = self.teachers.get(employee_id)
        if teacher:
            print(f"Employee ID: {teacher.employee_id}")
            print(f"Name: {teacher.name}")
            print(f"Age: {teacher.age}")
        else:
            print(f"Teacher with Employee ID {employee_id} not found.")

# Create a Head
head = Head("Prakash", 35, "RIT", "rit123")

# Creating teacher objects
teacher1 = Teacher("Ganesh", 30, "T101")
teacher2 = Teacher("Ramesh", 35, "T102")

# Creating student objects
student1 = Student("Abhijith", 21, "101")
student2 = Student("Jeevan", 21, "102")
student3 = Student("Shreyas", 21, "103")
student4 = Student("Fayaz", 21, "104")

# Creating a student database
database = StudentDatabase()
# Adding students and teachers to the database
database.add_student(student1)
database.add_student(student2)
database.add_student(student3)
database.add_student(student4)

database.add_teacher(teacher1)
database.add_teacher(teacher2)

while True:
    user_type = input("Are you a 'head', 'teacher', 'student', or 'quit'? ").lower()

    if user_type == 'quit':
        break

    if user_type == 'head':
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == head.username and password == head.password:
            while True:
                action = input("Add 'student', 'teacher', 'quit', 'list teachers', or 'list students' (to list students): ").lower()
                if action == 'quit':
                    break

                if action == 'student':
                    roll_no = input("Enter Student Roll No: ")
                    name = input("Enter Student Name: ")
                    age = int(input("Enter Student Age: "))
                    student = Student(name, age, roll_no)
                    database.add_student(student)
                    print("Student added successfully.")

                elif action == 'teacher':
                    employee_id = input("Enter Teacher Employee ID: ")
                    name = input("Enter Teacher Name: ")
                    age = int(input("Enter Teacher Age: "))
                    teacher = Teacher(name, age, employee_id)
                    database.add_teacher(teacher)
                    print("Teacher added successfully.")

                elif action == 'list teachers':
                    for emp_id, teacher in database.teachers.items():
                        print(f"Employee ID: {emp_id}, Name: {teacher.name}")

                elif action == 'list students':
                    for roll_no, student in database.students.items():
                        print(f"Roll No: {roll_no}, Name: {student.name}")

                else:
                    print("Invalid action. Please try again.")

        else:
            print("Authentication failed. Access denied.")

    elif user_type == 'teacher':
        # Implement teacher authentication and actions here
        pass

    elif user_type == 'student':
        roll_no_to_search = input("Enter your Roll No (or 'quit' to exit): ")
        if roll_no_to_search.lower() == 'quit':
            break
        database.display_student_details(roll_no_to_search)

    else:
        print("Invalid user type. Please try again.")
