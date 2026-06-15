from database import conn, cursor

def add_equipment(name, etype, manufacturer, model, serial, install_date, purchase_date, dept_id, status):
    sql = """
    INSERT INTO Equipment 
    (Equipment_Name, Equipment_Type, Manufacturer, Model_Number, Serial_Number, 
     Installation_Date, Purchase_Date, Department_ID, Status) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    # Changed the nine %s placeholders to ? for SQLite
    cursor.execute(sql, (name, etype, manufacturer, model, serial, install_date, purchase_date, dept_id, status))
    conn.commit()
