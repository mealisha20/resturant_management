from datetime import datetime
from .connection import get_connection

# ==================================================
# BILLING QUERIES
# ==================================================

def db_get_all():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM billings ORDER BY id DESC").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def db_get_one(billing_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM billings WHERE id = ?",(billing_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def db_create(data):
    conn = get_connection()
    now = datetime.now().isoformat()
    cur = conn.execute(
        "INSERT INTO billings (order_by, total_items, amount, created_at) VALUES (?, ?, ?, ?)",
        (data["order_by"], data["total_items"], data["amount"], now)
    )
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return db_get_one(new_id)


def db_update(billing_id, data):
    conn = get_connection()
    now = datetime.now().isoformat()
    conn.execute(
        "UPDATE billings SET order_by=?, total_items=?, amount=?, updated_at=? WHERE id=?",
        (data["order_by"], data["total_items"], data["amount"], now, billing_id)
    )
    conn.commit()
    conn.close()
    return db_get_one(billing_id)


def db_delete(billing_id):
    billing = db_get_one(billing_id)
    if not billing:
        return None

    conn = get_connection()
    conn.execute("DELETE FROM billings WHERE id=?", (billing_id,))
    conn.commit()
    conn.close()
    return billing

# ==================================================
# MENU QUERIES
# ==================================================

def db_get_all():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM menus ORDER BY name ASC").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def db_get_one(menu_name):
    conn = get_connection()
    row = conn.execute("SELECT * FROM menus WHERE name = ?", (menu_name,)).fetchone()
    conn.close()
    return dict(row) if row else None


def db_create(data):
    conn = get_connection()
    now = datetime.now().isoformat()
    cur = conn.execute(
        "INSERT INTO menus (name, price, rating, created_at) VALUES (?, ?, ?, ?)",
        (data["name"], data["price"], data["rating"], now)
    )
    conn.commit()
    new_name = cur.lastrowid
    conn.close()
    return db_get_one(new_name)


def db_update(menu_name, data):
    conn = get_connection()
    now = datetime.now().isoformat()
    conn.execute(
        "UPDATE menus SET price=?, rating=?, updated_at=? WHERE name=?",
        (data["price"], data["rating"], now, menu_name)
    )
    conn.commit()
    conn.close()
    return db_get_one(menu_name)


def db_delete(menu_name):
    menu = db_get_one(menu_name)
    if not menu:
        return None

    conn = get_connection()
    conn.execute("DELETE FROM menus WHERE name=?", (menu_name,))
    conn.commit()
    conn.close()
    return menu


# ==================================================
# STAFF QUERIES
# ==================================================

def db_get_all():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM staffs ORDER BY id DESC").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def db_get_one(staff_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM staffs WHERE id = ?", (staff_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def db_create(data):
    conn = get_connection()
    now = datetime.now().isoformat()
    cur = conn.execute(
        "INSERT INTO staffs (name, age, email, created_at) VALUES (?, ?, ?, ?)",
        (data["name"], data["age"], data["email"], now)
    )
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return db_get_one(new_id)


def db_update(staff_id, data):
    conn = get_connection()
    now = datetime.now().isoformat()
    conn.execute(
        "UPDATE staffs SET name=?, age=?, email=?, updated_at=? WHERE id=?",
        (data["name"], data["age"], data["email"], now, staff_id)
    )
    conn.commit()
    conn.close()
    return db_get_one(staff_id)


def db_delete(staff_id):
    staff = db_get_one(staff_id)
    if not staff:
        return None

    conn = get_connection()
    conn.execute("DELETE FROM staffs WHERE id=?", (staff_id,))
    conn.commit()
    conn.close()
    return staff
