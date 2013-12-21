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
    unspent = access.listunspent(0)
    balance = sum(map(lambda u: u["amount"], unspent))
    return balance

def get_context():
    return {
        "balance": get_balance()
    }  

# Page routes
@b.route('/')
def index():
    out_obj = get_context()
    return b.template('index', out_obj)

@b.route('/addresses/list/')
def address_list():
    out_obj = get_context()
    out_obj["addresses"] = access.getaddressesbyaccount("")
    return b.template('address_list', out_obj)

@b.route('/addresses/unspent/')
def address_unspent():
    out_obj = get_context()
    out_obj["unspent"] = access.listunspent(0)
    return b.template('address_unspent', out_obj)

@b.route('/addresses/received/')
def address_received():
    out_obj = get_context()
    addresses = access.listreceivedbyaddress(0)
    addresses = sorted(addresses, key=lambda k: k["amount"], reverse=True)
    for address in addresses:
        address["amount"] = '{0:.8f}'.format(address["amount"])
    out_obj["addresses"] = addresses
    return b.template('address_received', out_obj)

@b.route('/import/list/')
def import_list():
    out_obj = get_context()
    return b.template('import_list', out_obj)

b.run(host='loathes.asia', port=8080, debug=True)