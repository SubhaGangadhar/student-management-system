import json
from pathlib import Path

DATA_FILE = Path("students.json")


def load_students():
    """Load student records from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_students(students):
    """Save student records to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    student_id = input("Enter student ID: ").strip()

    if any(student["id"] == student_id for student in students):
        print("Student ID already exists.")
        return

    name = input("Enter student name: ").strip()
    age = input("Enter age: ").strip()
    course = input("Enter course: ").strip()
    email = input("Enter email: ").strip()

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "email": email
    }

    students.append(student)
    save_students(students)
    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n" + "-" * 85)
    print(f"{'ID':<12}{'Name':<20}{'Age':<8}{'Course':<20}{'Email':<25}")
    print("-" * 85)

    for student in students:
        print(
            f"{student['id']:<12}"
            f"{student['name']:<20}"
            f"{student['age']:<8}"
            f"{student['course']:<20}"
            f"{student['email']:<25}"
        )

    print("-" * 85)


def search_student(students):
    student_id = input("Enter student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found")
            print(f"ID     : {student['id']}")
            print(f"Name   : {student['name']}")
            print(f"Age    : {student['age']}")
            print(f"Course : {student['course']}")
            print(f"Email  : {student['email']}")
            return

    print("Student not found.")


def update_student(students):
    student_id = input("Enter student ID to update: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("Press Enter to keep the existing value.")

            name = input(f"Name [{student['name']}]: ").strip()
            age = input(f"Age [{student['age']}]: ").strip()
            course = input(f"Course [{student['course']}]: ").strip()
            email = input(f"Email [{student['email']}]: ").strip()

            if name:
                student["name"] = name
            if age:
                student["age"] = age
            if course:
                student["course"] = course
            if email:
                student["email"] = email

            save_students(students)
            print("Student updated successfully.")
            return

    print("Student not found.")


def delete_student(students):
    student_id = input("Enter student ID to delete: ").strip()

    for student in students:
        if student["id"] == student_id:
            confirm = input(
                f"Are you sure you want to delete {student['name']}? (y/n): "
            ).strip().lower()

            if confirm == "y":
                students.remove(student)
                save_students(students)
                print("Student deleted successfully.")
            else:
                print("Deletion cancelled.")
            return

    print("Student not found.")


def show_menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def main():
    students = load_students()

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

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
            print("Thank you for using Student Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
