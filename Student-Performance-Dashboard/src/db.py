from loader import cur, conn


def execute_write(query, params=()):
    cur.execute(query, params)
    conn.commit()

def execute_read(query , params=()):
    cur.execute(query, params)
    return cur.fetchall()


