from database import get_connection

connection = get_connection()

cursor = connection.cursor()

cursor.execute(""" 
    create table if not exists users (
        id serial primary key,
        name varchar(100),
        email VARCHAR(150)
    )""")

connection.commit()

cursor.close()
connection.close()

print("database connected successfully!")
print("users table created successfully!")