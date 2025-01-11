from bottle import run, default_app
from pedales.cogs import go

### Real sh1t ###
cogs = go()
from pedales import real

### APIs ###
from pedales import apis
apis.sh1t(cogs['modo'], cogs['db'])

### # ###
if __name__ == '__main__':
     if cogs['modo'] == 'dev':
          run(host='0.0.0.0', port=cogs['port'], debug=True, reloader=True)
     if cogs['modo'] == 'FTW':
          run(host='0.0.0.0', port=cogs['port'])

#ned
