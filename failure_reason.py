from database import conn, cursor

def add_failure_reason(category, description):
    sql = """
    INSERT INTO Failure_Reason (Failure_Category, Description) 
    VALUES (?, ?)
    """
    # Changed %s to ? for SQLite
    cursor.execute(sql, (category, description))
    conn.commit()

def get_failure_reasons():
    cursor.execute("SELECT Failure_ID, Failure_Category FROM Failure_Reason")
    return cursor.fetchall()
