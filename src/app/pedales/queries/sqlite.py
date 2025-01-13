import sqlite3

def call_db(query: str, query_params: tuple[str]) -> list[list] | None:
     con = sqlite3.connect('../../temp/Planner.db')
     query_result = con.execute(query, query_params).fetchall()
     con.close()
     return query_result
