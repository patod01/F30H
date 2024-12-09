from bottle import run, default_app
from pedales.cogs import go

### Real sh1t ###
modo, port = go()
from pedales import real

### APIs ###
from pedales import apis
apis.sh1t(modo)

### # ###
if __name__ == '__main__':
     if modo == 'dev':
          run(host='0.0.0.0', port=port, debug=True, reloader=True)
     if modo == 'FTW':
          run(host='0.0.0.0', port=port)

#ned
