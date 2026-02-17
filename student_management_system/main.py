from student import Student
from storage import load_students, save_students
from utils import print_menu, find_student

def add_student(students):
    student_id = input("Enter Student ID: ")
    if find_student(students, student_id):
        print("Student ID already exists!")
        return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = Student(student_id, name, age, course)
    students.append(student.to_dict())
    save_students(students)
    print("Student added successfully!")

def view_students(students):
    if not students:
        print("No students found.")
        return

    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s['student_id']} | Name: {s['name']} | Age: {s['age']} | Course: {s['course']}")

def search_student(students):
    student_id = input("Enter Student ID to search: ")
    student = find_student(students, student_id)

    if student:
        print("\nStudent Found:")
        print(student)
    else:
        print("Student not found.")

def update_student(students):
    student_id = input("Enter Student ID to update: ")
    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    student["name"] = input("Enter new name: ")
    student["age"] = input("Enter new age: ")
    student["course"] = input("Enter new course: ")

    save_students(students)
    print("Student updated successfully!")

def delete_student(students):
    student_id = input("Enter Student ID to delete: ")
    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    students.remove(student)
    save_students(students)
    print("Student deleted successfully!")

def main():
    students = load_students()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
