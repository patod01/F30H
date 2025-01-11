from bottle import error, route, static_file

ui_root = './pedales/ui'

@error(404)
def go_default(error):
     return 'notmyproblem .!.'

@route('/')
def landing():
     return static_file('index.html', root=f'{ui_root}')

@route('/_astro/<file:path>')
def static(file):
     return static_file(file, root=f'{ui_root}/_astro')

@route('/js/<file:path>')
def static(file):
     return static_file(file, root=f'{ui_root}/js')

@route('/icon.png')
def static():
     return static_file('icon.png', root=f'{ui_root}')

@route('/app')
def main_app():
     return static_file('app/index.html', root=f'{ui_root}')
