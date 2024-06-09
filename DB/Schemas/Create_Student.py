import psycopg2

conn = psycopg2.connect(database = "StudentDB", 
                        user = "studentuser", 
                        host= 'localhost',
                        password = "studentuser",
                        port = 5432)

cur = conn.cursor()
# Execute a command: create datacamp_courses table
create_student_table = cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    ID SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    age INTEGER,
    phone VARCHAR(50)
);
""")

# Make the changes to the database persistent
conn.commit()
# Close cursor and communication with the database
cur.close()
conn.close()