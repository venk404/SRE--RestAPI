import psycopg2


conn = psycopg2.connect(database = "StudentDB", 
                        user = "studentuser", 
                        host= 'localhost',
                        password = "studentuser",
                        port = 5432)

cur = conn.cursor()

def insertstudent(data: dict):
    try:
        insert_query = """
        INSERT INTO students (name, email, age, phone)
        VALUES (%s, %s, %s, %s)
        RETURNING ID;
        """
        cur.execute(insert_query, (data.name, data.email, data.age, data.phone))
        student_id = cur.fetchone()[0]
        conn.commit()
        return {"status": "success", "message": "Student inserted successfully", "student_id": student_id}
    except psycopg2.Error as e:
        conn.rollback()
        return {"status": "error", "message": str(e)}
    

def get_all_students():
    try:
        select_query = """
        SELECT * from  students;
        """
        cur.execute(select_query)
        students = cur.fetchall()
        conn.commit()
        if(len(students) > 0 or students == None):
            return {"status": "success", "message": "Student inserted successfully", "students": students}
        else:
            return {"status": "error","message": "No Data Present"}
    except psycopg2.Error as e:
        conn.rollback()
        return {"status": "error", "message": str(e)}

def get_student_by_Id(id):
    try:
        select_query = """
        SELECT * FROM students WHERE ID = %s;
        """
        cur.execute(select_query, (id,))
        students = cur.fetchone()
        conn.commit()
        if(len(students) > 0):
            return {"status": "success", "students": students}
        else:
            return {"status": "success","message": "No Data found"}
    except psycopg2.Error as e:
        conn.rollback()
        return {"status": "error", "message": str(e)}
    
def Update_student(id):
    try:
        update_query = f"""
        SELECT * from  students where ID = %s;
        """
        cur.execute(update_query,(id,))
        students = cur.fetchone()
        conn.commit()
        if(len(students) > 0):
            return {"status": "success", "students": students}
        else:
            return {"status": "success","message": "No Data found"}
    except psycopg2.Error as e:
        conn.rollback()
        return {"status": "error", "message": str(e)}


def delete_student(id):
    try:
        delete_query = f"""
        DELETE FROM students WHERE Id = %s;
        """
        cur.execute(delete_query,(id,))
        if cur.rowcount > 0:
            conn.commit()
            return {"status": "success", "message": "Student deleted successfully"}
        else:
            return {"status": "error", "message": "Student not found"}
    except psycopg2.Error as e:
        conn.rollback()
        return {"status": "error", "message": str(e)}
    

    
