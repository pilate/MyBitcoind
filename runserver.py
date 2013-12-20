from bitcoinrpc.authproxy import AuthServiceProxy

import bottle as b


# Setup
b.TEMPLATE_PATH.append("templates")
access = AuthServiceProxy("http://Pilate:password@127.0.0.1:8332")

# Static file routes
@b.get('/static/css/<filename:re:.*\.css>')
def static_css(filename):
    return b.static_file(filename, root='static/css')

@b.get('/static/js/<filename:re:.*\.js>')
def static_js(filename):
    return b.static_file(filename, root='static/js')

# Utility
def get_balance():
    return float(access.getbalance("", 0))

def get_context():
    return {
        "balance": get_balance()
    }  

# Page routes
@b.route('/')
def index():
    out_obj = get_context()
    return b.template('index', out_obj)

@b.route('/addresses/')
def index():
    out_obj = get_context()
    addresses = access.listreceivedbyaddress(0, True)
    addresses = sorted(addresses, key=lambda k: k["amount"], reverse=True)
    for address in addresses:
        address["amount"] = '{0:.8f}'.format(address["amount"])
    out_obj["addresses"] = addresses
    return b.template('addresses', out_obj)

b.run(host='loathes.asia', port=8080, debug=True)