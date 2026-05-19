student = {}

# Create
def create_student(name, id):
    student[id] = name
    print(f"student {name} with id {id} created")

# Read
def read_student():
    print("\nStudent records")
    for id, name in student.items():
        print(f"id : {id}, name : {name}")

# Update
def update_student(id, new_name):
    if id in student:
        student[id] = new_name
        print(f"student with id {id} updated to {new_name}")
    else:
        print("student not found")

# Delete
def delete_student(id):
    if id in student:
        del student[id]
        print(f"student with id {id} deleted")

    else:
        print("student not found")

# testing CRUD Operations

create_student("jai", 1)
read_student()
update_student(1, "vijay kumar")
read_student()
delete_student(1)
read_student()
