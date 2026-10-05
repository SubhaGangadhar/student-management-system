# student-management-system
Python-based Student Management System with CRUD operations and JSON data storage.

-----------------------------------------------------------------------------------------------------------------------------------------

# Student Management System using Python

A simple command-line based **Student Management System** developed using Python.

## Features

- Add a new student
- View all students
- Search for a student by ID
- Update student details
- Delete a student
- Store student data permanently using a JSON file

## Technologies Used

- Python 3
- JSON
- File Handling
- Functions
- Lists and Dictionaries
- CRUD Operations

## Project Structure

```text
student-management-system/
│
├── student_management.py
├── students.json
└── README.md
```

> `students.json` is created automatically when the program saves the first student record.

## How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the installation:

```bash
python --version
```

### 2. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 3. Open the project folder

```bash
cd student-management-system
```

### 4. Run the program

```bash
python student_management.py
```

## Menu

```text
===== Student Management System =====
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
```

## Example

```text
Enter student ID: S101
Enter student name: Rahul
Enter age: 22
Enter course: MCA
Enter email: rahul@example.com

Student added successfully.
```

## Concepts Demonstrated

This project demonstrates basic Python concepts that are useful for beginners and MCA interviews:

- Variables and data types
- Conditional statements
- Loops
- Functions
- Lists
- Dictionaries
- File handling
- JSON data storage
- Exception handling
- CRUD operations

## Future Improvements

The project can be extended by adding:

- Login/authentication
- SQLite or MySQL database
- Graphical user interface
- HTML/CSS frontend
- Flask web application
- Student marks and grades
- Attendance management

## Author

**SubhaGangadhar**

Created as a Python project for learning and portfolio development.
