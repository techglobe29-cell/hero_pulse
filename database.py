import sqlite3
import os

# 1. Connect to an automatically managed local database file
DB_FILE = "maintenance_system.db"
conn = sqlite3.connect(DB_FILE, check_same_thread=False)
cursor = conn.cursor()

# 2. Automatically build the tables if they don't exist yet
# This reads your schema.sql.txt file to set up the database
if os.path.exists("schema.sql.txt"):
    with open("schema.sql.txt", "r") as f:
        schema_sql = f.read()
    try:
        cursor.executescript(schema_sql)
        conn.commit()
    except Exception as e:
        # Tables might already exist, which is fine
        pass
