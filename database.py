import sqlite3

# 1. Connect to a BRAND NEW database file to bypass Streamlit's memory cache
conn = sqlite3.connect('hero_pulse_v2.db', check_same_thread=False)
cursor = conn.cursor()

# 2. Define the setup function that creates all tables
def init_db():
    
    # 🏢 Department Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Department (
        Department_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Department_Name TEXT NOT NULL,
        Location TEXT
    )
    """)
    
    # ⚙️ Equipment Table
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

    # 👷 Technician Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Technician (
        Technician_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Technician_Name TEXT NOT NULL,
        Phone TEXT,
        Email TEXT,
        Skill_Level TEXT
    )
    """)

    # ⚠️ Failure Reason Table (Updated with exact column names your app needs)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Failure_Reason (
        Failure_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Failure_Category TEXT NOT NULL,
        Description TEXT
    )
    """)

    # 🛠️ Corrective Action Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Corrective_Action (
        Action_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Action_Name TEXT NOT NULL,
        Description TEXT
    )
    """)

    # 🔧 Maintenance Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Maintenance (
