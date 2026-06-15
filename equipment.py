# 1. ALWAYS put your imports at the very top of the file!
from database import conn, cursor

# 2. Define your setup function
def init_db():
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

# 3. Run the setup function
init_db()

# 4. The rest of your functions go below...
def add_equipment(...):
    # ... your existing code ...
