import sqlite3

# 1. Connect to the database
conn = sqlite3.connect('hero_pulse.db', check_same_thread=False)
cursor = conn.cursor()

# 2. Define the comprehensive setup function
def init_db():
    # 🏢 Create Department Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Department (
        Department_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Department_Name TEXT NOT NULL,
        Location TEXT
    )
    """)
    
    # ⚙️ Create Equipment Table
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

    # 👷 Create Technician Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Technician (
        Technician_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Technician_Name TEXT NOT NULL,
        Phone TEXT,
        Email TEXT,
        Skill_Level TEXT
    )
    """)

    # ⚠️ Create Failure Reason Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Failure_Reason (
        Reason_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Category TEXT NOT NULL,
        Description TEXT
    )
    """)

    # 🛠️ Create Corrective Action Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Corrective_Action (
        Action_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Action_Name TEXT NOT NULL,
        Description TEXT
    )
    """)

    # 🔧 Create Maintenance Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Maintenance (
        Maintenance_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Equipment_ID INTEGER,
        Technician_ID INTEGER,
        Maintenance_Type TEXT,
        Scheduled_Date TEXT,
        Remarks TEXT,
        Status TEXT DEFAULT 'Scheduled'
    )
    """)

    # ⏱️ Create Downtime Table
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

    # Save all creations!
    conn.commit()

# 3. Run it immediately
init_db()
