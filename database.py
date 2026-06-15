import sqlite3

# 1. Connect to the database
conn = sqlite3.connect('hero_pulse.db', check_same_thread=False)
cursor = conn.cursor()

# 2. Define the table creation function
def init_db():
    # Create the Department table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Department (
        Department_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Department_Name TEXT NOT NULL,
        Location TEXT
    )
    """)
    
    # Create the Equipment table (so you don't get the error there next!)
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
        Status TEXT,
        FOREIGN KEY (Department_ID) REFERENCES Department(Department_ID)
    )
    """)
    
    # Save the changes
    conn.commit()

# 3. CRITICAL: Run the function immediately 
init_db()
