import sqlite3
p=r'C:\Users\shiha\Documents\DRF_Ecommerce_api\ecommerceBackend\db.sqlite3'
conn=sqlite3.connect(p)
print('Tables:', conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())
print('accountApp_customuser PRAGMA:', conn.execute("PRAGMA table_info('accountApp_customuser')").fetchall())
conn.close()
