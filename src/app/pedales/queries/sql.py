import os, sqlite3, time
from .sqlsrv import call_db as sqlsrv_call
from .sqlite import call_db as sqlite_call

query_b1 = \
     """\
     SELECT ccosto AS [PY], fecha AS [date], login AS [user], hh_proy AS [HH]
     FROM hh_py
     WHERE
          fecha >= ?
          AND fecha <= ?
          %s
     ORDER BY PY, date;
     """

def get_HH(req: dict, db: str) -> list[list] | None:
     query_b2 = f"AND ccosto IN ({', '.join(['?']*len(req['projects']))})"
     full_query = query_b1 % query_b2
     if not req['dates'][0] and not req['dates'][1]:
          req['dates'][1] = time.strftime('%Y-%m-%d', time.localtime())
     elif not req['dates'][1]:
          req['dates'][1] = req['dates'][0]
     query_params = *req['dates'], *req['projects'],
     print(req)
     print(query_params)
     print(full_query)
     if db == 'sqlite':
          return sqlite_call(full_query, query_params)
     elif db == 'sqlserver':
          return sqlsrv_call(full_query, query_params)
