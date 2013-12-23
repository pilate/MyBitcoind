from util import get_context

import bottle as b


address_app = b.Bottle()


@address_app.get('/list/')
def address_list():
    out_obj = get_context()
    rpc = out_obj["rpc"]
    addresses = []
    if rpc:
        addresses = rpc.getaddressesbyaccount("")
    out_obj["addresses"] = addresses
    return b.template('address_list', out_obj)

@address_app.get('/unspent/')
def address_unspent():
    out_obj = get_context()
    rpc = out_obj["rpc"]
    unspent = []
    if rpc:
        unspent = rpc.listunspent(0)
    out_obj["unspent"] = unspent
    return b.template('address_unspent', out_obj)

@address_app.get('/received/')
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
