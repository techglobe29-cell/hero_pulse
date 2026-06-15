import sqlite3

# 1. Create the connection (this creates a hero_pulse.db file if it doesn't exist)
conn = sqlite3.connect('hero_pulse.db', check_same_thread=False)
cursor = conn.cursor()

# 2. Define the setup function
def init_db():
    # Create Department Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Department (
        Department_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Department_Name TEXT NOT NULL,
        Location TEXT
    )
    """)
    
    # Create Equipment Table
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
    
    conn.commit()

# 3. Run the setup function immediately so tables exist before the app loads!
init_db()
