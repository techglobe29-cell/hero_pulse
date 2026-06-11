from database import conn, cursor

def add_department(name, location):
    sql = """
    INSERT INTO Department (Department_Name, Location)
    VALUES (%s, %s)
    """
    cursor.execute(sql, (name, location))
    conn.commit()

def get_departments():
    cursor.execute("SELECT Department_ID, Department_Name FROM Department")
    return cursor.fetchall()