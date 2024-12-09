import os, subprocess
from .kensten import kensten as knstn

if os.name == 'posix' \
and not os.path.isfile('./pedales/lin/_ok_'):
     with open('./pedales/lin/_ok_', 'w') as f:
          os.system('chmod -R +x ./pedales/lin')
          f.write('')

if not os.path.isdir('./AQUI'):
     os.mkdir('./AQUI')
if not os.path.isdir('./AQUI/reportes'):
     os.mkdir('./AQUI/reportes')

os_path, ext = ('lin', 'sh') if os.name == 'posix' else ('win', 'bat')
pedales = f'.{os.sep}pedales{os.sep}{os_path}{os.sep}'

### implement your shit here ###
def open_it():
     subprocess.run([pedales + f'open.{ext}'])

def load_it() -> int:
     sproc = subprocess.run([pedales + f'load.{ext}'], capture_output=1, text=1)
     return len(sproc.stdout.split('\n')) - 1

def kensten(): return knstn()
