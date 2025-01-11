import time, json, os
# import pyodbc

if os.path.isfile('__env.json'):
     with open('__env.json') as env:
          keys = json.load(env)
          print(keys)
else:
     with open('__env.json', 'w') as env:
          json.dump({
               "SERVER": '',
               "DATABASE": '',
               "UID": '',
               "PWD": '',
          }, env, indent=5)
     exit()

conn_pssr = (
     "DRIVER={SQL Server};"
     f"SERVER={keys['SERVER']};"
     f"DATABASE={keys['DATABASE']};"
     f"UID={keys['UID']};"
     f"PWD={keys['PWD']};"
     "Trusted_Connection=yes;"
)

exit()

t1 = time.time()

conn = pyodbc.connect(conn_pssr)

t2 = time.time()

SQL_QUERY = """
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

t3 = time.time()

records = cursor.fetchall()

t4 = time.time()

for r in records:
     print(r)

t5 = time.time()

print(f'connection time: {round(t2 - t1, 2)} s.')
print(f'excecution time: {round(t3 - t2, 2)} s.')
print(f'fetching time: {round(t4 - t3, 2)} s.')
print(f'printting time: {round(t5 - t4, 2)} s.')
