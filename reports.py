from database import cursor

def get_downtime_report():
    cursor.execute("""
        SELECT e.Equipment_Name, SUM(d.Duration_Hours) as Total_Downtime
        FROM Downtime d
        JOIN Equipment e ON d.Equipment_ID = e.Equipment_ID
        GROUP BY e.Equipment_Name
    """)
    return cursor.fetchall()

def get_maintenance_report():
    cursor.execute("""
        SELECT e.Equipment_Name, m.Maintenance_Type, m.Scheduled_Date, m.Status
        FROM Maintenance m
        JOIN Equipment e ON m.Equipment_ID = e.Equipment_ID
        ORDER BY m.Scheduled_Date DESC
    """)
    return cursor.fetchall()

def get_equipment_report():
    cursor.execute("""
        SELECT e.Equipment_Name, e.Equipment_Type, e.Manufacturer,
               e.Status, d.Department_Name
        FROM Equipment e
        LEFT JOIN Department d ON e.Department_ID = d.Department_ID
    """)
    return cursor.fetchall()

def get_technician_report():
    cursor.execute("""
        SELECT Technician_Name, Phone, Email, Skill_Level
        FROM Technician
    """)
    return cursor.fetchall()

def get_department_report():
    cursor.execute("""
        SELECT Department_Name, Location
        FROM Department
    """)
    return cursor.fetchall()

def get_failure_report():
    cursor.execute("""
        SELECT f.Failure_Category, COUNT(d.Downtime_ID) as Occurrences
        FROM Failure_Reason f
        LEFT JOIN Downtime d ON f.Failure_ID = d.Failure_ID
        GROUP BY f.Failure_Category
        ORDER BY Occurrences DESC
    """)
    return cursor.fetchall()

def get_action_report():
    cursor.execute("""
        SELECT a.Action_Name, COUNT(d.Downtime_ID) as Times_Used
        FROM Corrective_Action a
        LEFT JOIN Downtime d ON a.Action_ID = d.Action_ID
        GROUP BY a.Action_Name
        ORDER BY Times_Used DESC
    """)
    return cursor.fetchall()