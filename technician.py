from database import conn, cursor

def add_technician(name, phone, email, skill_level):
    sql = """
    INSERT INTO Technician (Technician_Name, Phone, Email, Skill_Level)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (name, phone, email, skill_level))
    conn.commit()

def get_technicians():
    cursor.execute("SELECT Technician_ID, Technician_Name FROM Technician")
    return cursor.fetchall()