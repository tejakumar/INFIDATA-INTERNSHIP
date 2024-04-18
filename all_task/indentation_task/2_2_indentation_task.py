class Student:
    def __init__(self, roll_no, name, age, grade):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def accept_student(self):
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        grade = input("Enter Grade: ")
        student = Student(roll_no, name, age, grade)
        self.students.append(student)
        print("Student record added successfully!")

    def display_students(self):
        if not self.students:
            print("No student records found.")
        else:
            print("Student Records:")
            for student in self.students:
                print(f"Roll No: {student.roll_no}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print(f"Student Found - Roll No: {student.roll_no}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
                return
        print("Student not found!")

    def delete_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print(f"Student with Roll No {roll_no} deleted successfully!")
                return
        print("Student not found!")

    def update_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print("Enter new student information:")
                name = input("Enter Name: ")
                age = input("Enter Age: ")
                grade = input("Enter Grade: ")
                student.name = name
                student.age = age
                student.grade = grade
                print(f"Student with Roll No {roll_no} updated successfully!")
                return
        print("Student not found!")

def main():
    sms = StudentManagementSystem()
    while True:
        print("\nStudent Management System Menu:")
        print("1. Accept Student Record")
        print("2. Display Student Records")
        print("3. Search Student Record")
        print("4. Delete Student Record")
        print("5. Update Student Record")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            sms.accept_student()
        elif choice == "2":
            sms.display_students()
        elif choice == "3":
            roll_no = input("Enter Roll No to search: ")
            sms.search_student(roll_no)
        elif choice == "4":
            roll_no = input("Enter Roll No to delete: ")
            sms.delete_student(roll_no)
        elif choice == "5":
            roll_no = input("Enter Roll No to update: ")
            sms.update_student(roll_no)
        elif choice == "6":
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()