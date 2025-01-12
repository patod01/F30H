from pedales.powers import open_it, load_it, kensten
from bottle import request, response, route
from .queries.sql import get_HH

def sh1t(modo: str, db: str) -> None:
     methods = ['OPTIONS', 'GET'] if modo == 'dev' else ['GET']
     @route('/ejecuta/<accion>', method=methods)
     def ejecuta(accion):
          if modo == 'dev':
               response.headers['Access-Control-Allow-Origin'] = '*'
               response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
               if request.method == 'OPTIONS': return
               print('dev CORS')
          match accion:
               case 'abrir-xlsx':
                    open_it()
                    return {"action": 'barido'}
               case 'cargar-xlsx':
                    return {"action": 'cargar', "total_files": load_it()}
               case 'kensten':
                    formatted = kensten()
                    return {
                         "action": 'kennen',
                         "discarded": formatted[0],
                         "formatted": formatted[1]
                    }
          return {"wholesome": 'pete'}

     methods = ['OPTIONS', 'POST'] if modo == 'dev' else ['POST']
     @route('/buscar_personas', method=methods)
     def buscar_personas():
          if modo == 'dev':
               response.headers['Access-Control-Allow-Origin'] = '*'
               response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
               if request.method == 'OPTIONS': return
               print('dev CORS')

          # print(request.json)
          return {"data": get_HH(request.json, db)}
          return {"wholesome": 'pete'}
     return
