# Opens a connection to SQLite and returns it for DB operations

import sqlite3

DB_FILE = "restaurant.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_database():
    conn = get_connection()
    conn.execute(""" 
        CREATE TABLE IF NOT EXISTS billings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_by TEXT,
            total items INTEGER,
            amount INTEGER
            
        ) 
    """)

    conn.execute(""" 
        CREATE TABLE IF NOT EXISTS menus (
            name TEXT,
            price INTEGER,
            rating INTEGER
            
        ) 
    """)

    conn.execute(""" 
        CREATE TABLE IF NOT EXISTS staffs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,     
            email TEXT
            
        ) 
    """)
    conn.commit()
    conn.close()
    print("✓ Database initialized")        