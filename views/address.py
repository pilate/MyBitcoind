from datetime import datetime
from plugins import BitcoinRPCPlugin
from plugins import ContextPlugin

import bottle as b


address_app = b.Bottle()
address_app.install(BitcoinRPCPlugin())
address_app.install(ContextPlugin())


def from_timestamp(time):
    return datetime.fromtimestamp(time)


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

@address_app.get("/recent/")
def address_recent(rpc, context):
    recent = []
    if rpc:
        recent = rpc.listtransactions("", 50)
        recent = filter(lambda r: "otheraccount" not in r, recent)
        for transaction in recent:
            if "blocktime" in transaction:
                transaction["realtimestamp"] = transaction["blocktime"]
                transaction["realtime"] = from_timestamp(transaction["blocktime"])
            elif "time" in transaction:
                transaction["realtimestamp"] = transaction["time"]
                transaction["realtime"] = from_timestamp(transaction["time"])
        recent = sorted(recent, key=lambda r: r["realtimestamp"], reverse=True)
    context["recent"] = recent
    return b.template("address_recent", context)