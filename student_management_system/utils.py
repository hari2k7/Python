def print_menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def find_student(students, student_id):
    for student in students:
        if student["student_id"] == student_id:
            return student
    return None
