def init_db():
    # This ensures the table exists before you try to pull data from it!
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Department (
        Department_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Department_Name TEXT NOT NULL,
        Location TEXT
    )
    """)
    conn.commit()

# Call this immediately after connecting to your database
init_db()
