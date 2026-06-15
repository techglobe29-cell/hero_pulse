import sqlite3

conn = sqlite3.connect('hero_pulse_v2.db', check_same_thread=False)
cursor = conn.cursor()

def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Department (
        Department_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Department_Name TEXT NOT NULL,
        Location TEXT
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Equipment (
        Equipment_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Equipment_Name TEXT NOT NULL,
        Equipment_Type TEXT,
        Manufacturer TEXT,
        Model_Number TEXT,
        Serial_Number TEXT,
        Installation_Date TEXT,
        Purchase_Date TEXT,
        Department_ID INTEGER,
        Status TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Technician (
        Technician_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Technician_Name TEXT NOT NULL,
        Phone TEXT,
        Email TEXT,
        Skill_Level TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Failure_Reason (
        Failure_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Failure_Category TEXT NOT NULL,
        Description TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Corrective_Action (
        Action_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Action_Name TEXT NOT NULL,
        Description TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Maintenance (
        Maintenance_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Equipment_ID INTEGER,
        Technician_ID INTEGER,
        Maintenance_Type TEXT,
        Scheduled_Date TEXT,
        Status TEXT,
        Remarks TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Downtime (
        Downtime_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Equipment_ID INTEGER,
        Start_Time TEXT,
        End_Time TEXT,
        Duration REAL,
        Failure_ID INTEGER,
        Action_ID INTEGER
    )
    """)
    conn.commit()

init_db()
