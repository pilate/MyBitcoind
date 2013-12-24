from plugins import BitcoinRPCPlugin
from util import get_context

import bottle as b


address_app = b.Bottle()
address_app.install(BitcoinRPCPlugin())


@address_app.route('/list/')
def address_list(rpc):
    out_obj = get_context(rpc)
    addresses = []
    if rpc:
        addresses = rpc.getaddressesbyaccount("")
    out_obj["addresses"] = addresses
    return b.template('address_list', out_obj)

@address_app.get('/unspent/')
def address_unspent(rpc):
    out_obj = get_context(rpc)
    unspent = []
    if rpc:
        unspent = rpc.listunspent(0)
    out_obj["unspent"] = unspent
    return b.template('address_unspent', out_obj)

@address_app.get('/received/')
def address_received(rpc):
    out_obj = get_context(rpc)
    addresses = []
    if rpc:
        addresses = rpc.listreceivedbyaddress(0)
        addresses = sorted(addresses, key=lambda k: k["amount"], reverse=True)
        for address in addresses:
            address["amount"] = '{0:.8f}'.format(address["amount"])
    out_obj["addresses"] = addresses
    return b.template('address_received', out_obj)
