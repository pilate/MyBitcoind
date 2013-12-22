from bitcoinrpc.authproxy import AuthServiceProxy
from bitcoinrpc.authproxy import JSONRPCException
from socket import timeout
from socket import error

import bottle as b


# Setup
b.TEMPLATE_PATH.append("templates")

# Static file routes
@b.get('/static/css/<filename:re:.*\.css>')
def static_css(filename):
    return b.static_file(filename, root='static/css')

@b.get('/static/js/<filename:re:.*\.js>')
def static_js(filename):
    return b.static_file(filename, root='static/js')

# Utility
def get_balance(rpc):
    unspent = rpc.listunspent(0)
    balance = sum(map(lambda u: u["amount"], unspent))
    return balance

def get_context():
    message = None
    try:
        rpc_connection = AuthServiceProxy("http://Pilate:password@127.0.0.1:8332", timeout=1)
        rpc_connection.getinfo()
    except timeout:
        rpc_connection = None
        message = {
            "text": "Bitcoind connection timeout.",
            "type": "warning"
        }
    except error:
        rpc_connection = None
        message = {
            "text": "Bitcoind connection refused.",
            "type": "warning"
        }

    if rpc_connection:
        balance = get_balance(rpc_connection)
    else:
        balance = "Error"

    return {
        "balance": balance,
        "message": message,
        "rpc": rpc_connection
    }  

# Address related routes
@b.get('/')
def index():
    out_obj = get_context()
    return b.template('index', out_obj)

@b.get('/addresses/list/')
def address_list():
    out_obj = get_context()
    rpc = out_obj["rpc"]
    addresses = []
    if rpc:
        addresses = rpc.getaddressesbyaccount("")
    out_obj["addresses"] = addresses
    return b.template('address_list', out_obj)

@b.get('/addresses/unspent/')
def address_unspent():
    out_obj = get_context()
    rpc = out_obj["rpc"]
    unspent = []
    if rpc:
        unspent = rpc.listunspent(0)
    out_obj["unspent"] = unspent
    return b.template('address_unspent', out_obj)

@b.get('/addresses/received/')
def address_received():
    out_obj = get_context()
    rpc = out_obj["rpc"]
    addresses = []
    if rpc:
        addresses = rpc.listreceivedbyaddress(0)
        addresses = sorted(addresses, key=lambda k: k["amount"], reverse=True)
        for address in addresses:
            address["amount"] = '{0:.8f}'.format(address["amount"])
    out_obj["addresses"] = addresses
    return b.template('address_received', out_obj)

# Import related routes
@b.get('/import/list/')
def import_list():
    out_obj = get_context()
    out_obj["privkeys"] = ""
    return b.template('import_list', out_obj)

@b.post('/import/list/')
def import_list():
    out_obj = get_context()
    out_obj["privkeys"] = ""
    rpc = out_obj["rpc"]
    form_addresses = b.request.forms.get('privkeys')
    split_addresses = form_addresses.split("\n");
    clean_list = map(str.strip, split_addresses)
    if rpc:
        added = 0
        for key in clean_list:
            rescan = False
            if key == clean_list[-1]:
                rescan = True
            try:
                rpc.importprivkey(key, "", rescan)
            except JSONRPCException:
                continue
            else:
                added += 1
        out_obj["message"] = {
            "text": "Imported {0} new keys. Rescan started.".format(added),
            "type": "info"
        }
    else:
        out_obj["privkeys"] = form_addresses
    return b.template('import_list', out_obj)

b.run(host='loathes.asia', port=8080, debug=True, reloader=True)