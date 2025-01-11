def go() -> dict[str, int | str]:
     import json, sys
     with open('settings/cogs.json') as cogs:
          _ = json.load(cogs)
          modo = _['modo']
          port = int(_['port'])
          db = _['db']
     if len(sys.argv) == 3:
          print('loading cli params')
          modo = sys.argv[1]
          port = int(sys.argv[2])
     print(f'Running in {modo} mode on port {port}...')
     print(f'Connection kind: {db}')
     return {"modo": modo, "port": port, "db": db}
