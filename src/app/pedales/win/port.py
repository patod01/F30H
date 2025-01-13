import os, json

with open('settings/cogs.json') as _:
     with open('settings/__prt.txt', 'w') as __:
          __.write(str(json.load(_)['port']))
