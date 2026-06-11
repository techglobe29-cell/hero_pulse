from database import conn, cursor

def log_downtime(equipment_id, start_time, end_time, duration, failure_id, action_id):
    sql = """
    INSERT INTO Downtime
    (Equipment_ID, Start_Time, End_Time, Duration_Hours, Failure_ID, Action_ID)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (equipment_id, start_time, end_time, duration, failure_id, action_id))
    conn.commit()