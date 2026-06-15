from database import conn, cursor

def add_department(name, location):
    sql = """
    INSERT INTO Department (Department_Name, Location)
    VALUES (?, ?) 
    """
    # Changed %s to ? for SQLite compatibility
    cursor.execute(sql, (name, location))
    conn.commit()

def get_departments():
    # This code was already correct!
    cursor.execute("SELECT Department_ID, Department_Name FROM Department")
    return cursor.fetchall()
