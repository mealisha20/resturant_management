# Contains business logic (validation, processing, rules)
# Does NOT know about HTTP — only works with Python data
# ---------- billing ----------
from database.queries import (
     db_get_all
    , db_get_one
    , db_create
    , db_update
    , db_delete
)

def service_get_all():
    return db_get_all()

def service_get_one(billing_id):
    return db_get_one(billing_id)

def service_create(data):
    return db_create(data)

def service_update(billing_id, data):
    return db_update(billing_id, data)

def service_delete(billing_id):
    return db_delete(billing_id)

# ---------- menu ----------
from database.queries import (
     db_get_all
    , db_get_one
    , db_create
    , db_update
    , db_delete
)


def service_get_all():
    return db_get_all()

def service_get_one(menu_name):
    return db_get_one(menu_name)

def service_create(data):
    return db_create(data)

def service_update(menu_name, data):
    return db_update(menu_name, data)

def service_delete(menu_name):
    return db_delete(menu_name)

# ---------- staff ----------
from database.queries import (
     db_get_all
    , db_get_one
    , db_create
    , db_update
    , db_delete
)

def service_get_all():
    return db_get_all()

def service_get_one(staff_id):
    return db_get_one(staff_id)

def service_create(data):
    return db_create(data)

def service_update(staff_id, data):
    return db_update(staff_id, data)

def service_delete(staff_id):
    return db_delete(staff_id)