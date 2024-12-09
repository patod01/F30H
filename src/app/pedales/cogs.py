def go() -> (str, int):
     import json, os, sys
     # if os.name == 'posix':
     #      ...
     # else:
     #      ...
     if len(sys.argv) == 1:
          with open('settings/cogs.json') as cogs:
               _ = json.load(cogs)
               modo = _['modo']
               port = int(_['port'])
     elif len(sys.argv) == 3:
          modo = sys.argv[1]
          port = int(sys.argv[2])
     else:
          raise Exception('EXPLODE')
     print(f'Running in {modo} mode on port {port}...')
     return modo, port
