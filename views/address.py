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
        transactions = {}
        recent = rpc.listtransactions("", 50)
        recent = filter(lambda r: "otheraccount" not in r, recent)
        for transaction in recent:
            txid = transaction["txid"]
            if txid not in transactions:
                transactions[txid] = {
                    "addresses": [],
                    "categories": [],
                    "amounts": []
                }
            transactions[txid]["addresses"].append(transaction["address"])
            transactions[txid]["categories"].append(transaction["category"])
            transactions[txid]["amounts"].append(transaction["amount"])
            if "blocktime" in transaction:
                transactions[txid]["realtimestamp"] = transaction["blocktime"]
                transactions[txid]["realtime"] = from_timestamp(transaction["blocktime"])
            elif "time" in transaction:
                transactions[txid]["realtimestamp"] = transaction["time"]
                transactions[txid]["realtime"] = from_timestamp(transaction["time"])
        grouped = []
        for txid, data in transactions.iteritems():
            data["txid"] = txid
            grouped.append(data)
        
        recent = sorted(grouped, key=lambda r: r["realtimestamp"], reverse=True)
    context["recent"] = recent
    return b.template("address_recent", context)