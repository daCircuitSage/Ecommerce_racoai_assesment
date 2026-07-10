import sqlite3
p='ecommerceBackend/db.sqlite3'
conn=sqlite3.connect(p)
print('Tables:', conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())
print('accountApp_customuser PRAGMA:', conn.execute("PRAGMA table_info('accountApp_customuser')").fetchall())
conn.close()
