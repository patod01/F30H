import os, sqlite3, time

query_b1 = \
     """\
     SELECT ccosto as PY, date, user, HH FROM hh_py
     WHERE
          date >= ?
          AND date <= ?
     %s
     ORDER BY PY, date;
     """

def get_HH(req):
     query_b2 = f"AND PY IN ({', '.join(['?']*len(req['projects']))})"
     query = query_b1 % query_b2
     if not req['dates'][0] and not req['dates'][1]:
          req['dates'][1] = time.strftime('%Y-%m-%d', time.localtime())
     elif not req['dates'][1]:
          req['dates'][1] = req['dates'][0]
     query_params = *req['dates'], *req['projects'],
     con = sqlite3.connect('../../temp/Planner.db')
     query_result = con.execute(query, query_params).fetchall()
     con.close()
     # for a in query_result: print(a)
     print(req)
     print(query_params)
     print(query)
     # time.sleep(2)
     return query_result
