# from loader import cur, conn


# def execute_write(query, params=()):
#     cur.execute(query, params)
#     conn.commit()

# def execute_read(query , params=()):
#     cur.execute(query, params)
#     return cur.fetchall()


import sqlite3

DB_PATH = "Performance.db"

def execute_write(query, params=()):
    # check_same_thread = False allows multiple threads to access the database connection
    conn = sqlite3.connect(DB_PATH, check_same_thread = True)
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    conn.close()


def execute_read(query, params=()):
    conn = sqlite3.connect(DB_PATH, check_same_thread = True)
    cur = conn.cursor()
    cur.execute(query, params)
    rows = cur.fetchall()
    conn.close()
    return rows
