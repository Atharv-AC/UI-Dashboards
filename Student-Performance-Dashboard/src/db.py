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
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    conn.close()


def execute_read(query, params=()):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(query, params)
    rows = cur.fetchall()
    conn.close()
    return rows
