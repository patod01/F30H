import json, os, time

if os.name != 'posix':
     import pyodbc

def to_data(raw_row) -> list | None:
     [project, date, user, HH] = raw_row
     return [
          project,
          f'{date.year}-{date.month:02}-{date.day:02}',
          user,
          float(HH)
     ]

def call_db(query: str, query_params: tuple[str]) -> list[list] | None:
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
     # print(conn_key)
     t1 = time.time()

     try:
          conn = pyodbc.connect(conn_key)
          cursor = conn.cursor()
          t2 = time.time()

          cursor.execute(query, query_params)
          t3 = time.time()

          records = cursor.fetchall()
          t4 = time.time()

          query_result = [to_data(r) for r in records]
          # for r in query_result[0:5]:
               # print(((r)))
          t5 = time.time()
     except Exception as e:
          print(e)
     finally:
          if 'cursor' in locals():
               cursor.close()
          if 'conn' in locals():
               conn.close()
          # print('cnn closed')

     print(f'connection time: {round(t2 - t1, 2)} s.')
     print(f'excecution time: {round(t3 - t2, 2)} s.')
     print(f'fetching time: {round(t4 - t3, 2)} s.')
     print(f'converting time: {round(t5 - t4, 2)} s.')

     return query_result


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
