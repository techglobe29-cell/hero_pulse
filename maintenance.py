from database import conn, cursor

def add_maintenance(equipment_id, technician_id, mtype, scheduled_date, remarks):
    sql = """
    INSERT INTO Maintenance
    (Equipment_ID, Technician_ID, Maintenance_Type, Scheduled_Date, Status, Remarks)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (equipment_id, technician_id, mtype, scheduled_date, "Scheduled", remarks))
    conn.commit()