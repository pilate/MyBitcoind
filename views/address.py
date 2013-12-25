from plugins import BitcoinRPCPlugin
from plugins import ContextPlugin

import bottle as b


address_app = b.Bottle()
address_app.install(BitcoinRPCPlugin())
address_app.install(ContextPlugin())


@address_app.route("/list/")
def address_list(rpc, context):
    addresses = []
    if rpc:
        addresses = rpc.getaddressesbyaccount("")
    context["addresses"] = addresses
    return b.template("address_list", context)

@address_app.get("/unspent/")
def address_unspent(rpc, context):
    unspent = []
    if rpc:
        unspent = rpc.listunspent(0)
    context["unspent"] = unspent
    return b.template("address_unspent", context)

@address_app.get("/received/")
def address_received(rpc, context):
    addresses = []
    if rpc:
        addresses = rpc.listreceivedbyaddress(0)
        addresses = sorted(addresses, key=lambda k: k["amount"], reverse=True)
        for address in addresses:
            address["amount"] = "{0:.8f}".format(address["amount"])
    context["addresses"] = addresses
    return b.template("address_received", context)
