from database import conn, cursor

def log_downtime(equipment_id, start_time, end_time, duration, failure_id, action_id):
    sql = """
    INSERT INTO Downtime 
    (Equipment_ID, Start_Time, End_Time, Duration, Failure_ID, Action_ID) 
    VALUES (?, ?, ?, ?, ?, ?)
    """
    # Changed %s to ? and updated Duration_Hours to Duration
    cursor.execute(sql, (equipment_id, start_time, end_time, duration, failure_id, action_id))
    conn.commit()
