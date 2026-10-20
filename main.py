
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

conn.commit()

#C: CREATION
def add_data(name,age):
    cursor.execute(
        "INSERT INTO students (name, age) VALUES (?, ?)",
        (name, age)
    )
    conn.commit()
    print("Student added successfully!")

#R: READ
def view_database():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    for student in students:
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}\n")

#U: UPDATE
def update_data(student_id, new_age):
    cursor.execute(
        "UPDATE students SET age = ? WHERE id = ?",
        (new_age, student_id)
    )
    conn.commit()

    if cursor.rowcount > 0:
        print("Data Updated successfully!")
    else:
        print("Student not found!")

#D: DELETE
def delete_data(student_id):
    cursor.execute (
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    deleted_count = cursor.rowcount
    conn.commit()

    if deleted_count > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found!")

loop = True

while(loop):
    user_input = input("Enter \n 1 for Creation \n 2 for Reading \n 3 for Updation \n 4 for Deletion \n (Type 'exit' to quit): ")

    if user_input == '1':
        num = int(input("Enter the number of new data values to add: "))
        for i in range(0,num):
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            add_data(name,age)

    elif user_input == '2':
        view_database()

    elif user_input == '3':
        u_id = int(input("Enter the student id to update: "))
        u_age = int(input("Enter the new age data for updation: "))
        update_data(u_id,u_age)

    elif user_input == '4':
         d_id = int(input("Enter the student id to delete: "))
         delete_data(d_id)

    elif user_input.lower() == 'exit':
        loop = False

    else:
        print("Invalid input!")


conn.close()

