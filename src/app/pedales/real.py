from bottle import error, route, static_file

@error(404)
def go_default(error):
     return 'notmyproblem .!.'

@route('/')
def landing():
     return static_file('index.html', root='./pedales/ui')

@route('/_astro/<file:path>')
def static(file):
     return static_file(file, root='./pedales/ui/_astro')

@route('/js/<file:path>')
def static(file):
     return static_file(file, root='./pedales/ui/js')

@route('/icon.png')
def static():
     return static_file('icon.png', root='./pedales/ui')
