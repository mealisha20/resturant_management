##################### API Observation Via Codespace URL
##################### API Observation Via Hopscotch
##################### API Observation Via CURL
# ==================================================
# BILLING 
# ==================================================

# A. Get All billings
curl -X GET "https://scaling-fortnight-v69p69x7rx552xw47-8000.app.github.dev/api/billings"

# B. Get One billing
curl -X GET "https://scaling-fortnight-v69p69x7rx552xw47-8000.app.github.dev/api/billings/1"

# C. Create billing
curl -X POST "https://scaling-fortnight-v69p69x7rx552xw47-8000.app.github.dev/api/billings" \
  -H "Content-Type: application/json" \
  -d '{
    "Total items": "8",
    "id": "1678f",
    "Amount": "657",
  }'

# D. Update billing
curl -X PUT "https://scaling-fortnight-v69p69x7rx552xw47-8000.app.github.dev/api/billings/2" \
  -H "Content-Type: application/json" \
  -d '{
    "Total items": "30",
    "id": "rtgf5657",
    "Amount": "4577",
  }'

# E. Delete billing
curl -X DELETE "https://scaling-fortnight-v69p69x7rx552xw47-8000.app.github.dev/api/billings/1"


# ==================================================
# MENU 
# ==================================================

# A. Get All menus
curl -X GET "https://scaling-fortnight-v69p69x7rx552xw47-8000.app.github.dev/api/menus"


# B. Get One menu
curl -X GET "https://scaling-fortnight-v69p69x7rx552xw47-8000.app.github.dev/api/menus/1"

# C. Create menu
curl -X POST "https://scaling-fortnight-v69p69x7rx552xw47-8000.app.github.dev/api/menus" \
  -H "Content-Type: application/json" \
  -d '{
    " name"="fhghgh", 
     "rating": "4",
     "price"="65"
    
  }'

# D. Update menu
curl -X PUT "https://scaling-fortnight-v69p69x7rx552xw47-8000.app.github.dev/api/menus/2" \
  -H "Content-Type: application/json" \
  -d '{
    " name"="aiswariya bhat", 
     "rating": "4",
     "price"="65"
    
  }'

# E. Delete menu
curl -X DELETE "https://scaling-fortnight-v69p69x7rx552xw47-8000.app.github.dev/api/menus/1"


# ==================================================
# STAFF 
# ==================================================
#  A. Get All staffs
curl -X GET "https://scaling-fortnight-v69p69x7rx552xw47-8000.app.github.dev/api/staffs"


# B. Get One staff
curl -X GET "https://scaling-fortnight-v69p69x7rx552xw47-8000.app.github.dev/api/staffs/1"

# C. Create staff
curl -X POST "https://scaling-fortnight-v69p69x7rx552xw47-8000.app.github.dev/api/staffs" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "ria",
    "age": "16",
    "emaile": "ria@gamil.com",
  }'

# D. Update staff
curl -X PUT "https://scaling-fortnight-v69p69x7rx552xw47-8000.app.github.dev/api/staffs/2" \
  -H "Content-Type: application/json" \
  -d '{
     "name": "ria",
    "age": "45",
    "emaile": "ria@gamil.com",
  }'

# E. Delete staff
curl -X DELETE "https://scaling-fortnight-v69p69x7rx552xw47-8000.app.github.dev/api/staffs/1"

##################### DB Observation Via SQLite Web
- install https://github.com/coleifer/sqlite-web
- pip install sqlite-web
- sqlite_web students.db