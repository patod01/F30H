import time, json, os
# import pyodbc

def call_db(query: str, query_params: tuple) -> list[list] | None:
     if os.path.isfile('settings/cogs.json'):
          with open('settings/cogs.json') as _:
               keys = json.load(_)
     conn_key = (
          "DRIVER={SQL Server};"
          f"SERVER={keys['SERVER']};"
          f"DATABASE={keys['DATABASE']};"
          f"UID={keys['UID']};"
          f"PWD={keys['PWD']};"
          "Trusted_Connection=yes;"
     )
     print(conn_key)
     return
     t1 = time.time()

     try:
          conn = pyodbc.connect(conn_key)
          cursor = conn.cursor()
          t2 = time.time()

          SQL_QUERY = ''
          cursor.execute(SQL_QUERY)
          t3 = time.time()

          records = cursor.fetchall()
          t4 = time.time()

          # for r in records:
          #      print(r)
          # t5 = time.time()

          cursor.close()
     except Exception as e:
          print(e)
     finally:
          conn.close()
          print('cn closed')

     print(f'connection time: {round(t2 - t1, 2)} s.')
     print(f'excecution time: {round(t3 - t2, 2)} s.')
     print(f'fetching time: {round(t4 - t3, 2)} s.')
     # print(f'printting time: {round(t5 - t4, 2)} s.')


def temporal():
     # if os.path.isfile('__env.json'):
     #      with open('__env.json') as env:
     #           keys = json.load(env)
     #           print(keys)
     # else:
     #      with open('__env.json', 'w') as env:
     #           json.dump({
     #                "SERVER": '',
     #                "DATABASE": '',
     #                "UID": '',
     #                "PWD": '',
     #           }, env, indent=5)
     exit()
