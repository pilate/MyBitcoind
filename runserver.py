import bottle as b

b.TEMPLATE_PATH.append("templates")

# Static file routes

@b.get('/static/css/<filename:re:.*\.css>')
def static_css(filename):
    return b.static_file(filename, root='static/css')

@b.get('/static/js/<filename:re:.*\.js>')
def static_js(filename):
    return b.static_file(filename, root='static/js')

# Page routes

@b.route('/')
def index():
    return b.template('index', {
        "balance": 0.1
    })

@b.route('/addresses/')
def index():
    return b.template('index', {
        "balance": 0.1
    })

b.run(host='localhost', port=8080)