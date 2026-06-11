from database import conn, cursor

def add_corrective_action(name, description):
    sql = """
    INSERT INTO Corrective_Action (Action_Name, Description)
    VALUES (%s, %s)
    """
    cursor.execute(sql, (name, description))
    conn.commit()

def get_corrective_actions():
    cursor.execute("SELECT Action_ID, Action_Name FROM Corrective_Action")
    return cursor.fetchall()