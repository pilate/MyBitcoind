from datetime import datetime
from plugins import BitcoinRPCPlugin
from plugins import ContextPlugin

import bottle as b


address_app = b.Bottle()
address_app.install(BitcoinRPCPlugin())
address_app.install(ContextPlugin())


def from_timestamp(time):
    return datetime.fromtimestamp(time)

def gather_tx(rpc, txid):
    ret_obj = {
        "txid": txid,
        "inputs": [],
        "outputs": []
    }

    raw_tx = rpc.getrawtransaction(txid, 1)
    ret_obj["time"] = from_timestamp(raw_tx["blocktime"])
    ret_obj["rawtime"] = raw_tx["blocktime"]
    for in_tx in raw_tx["vin"]:
        raw_in_tx = rpc.getrawtransaction(in_tx["txid"], 1)
        in_out = filter(lambda r: r["n"] == in_tx["vout"], raw_in_tx["vout"])[0]
        ret_obj["inputs"].append(in_out)
    for out_tx in raw_tx["vout"]:
        ret_obj["outputs"].append(out_tx)
    return ret_obj        

@address_app.route("/list/")
def address_list(rpc, context):
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
        recent_list = rpc.listtransactions("", 50)
        recent_list = filter(lambda r: "otheraccount" not in r, recent_list)
        recent_txids = filter(bool, set(map(lambda r: r["txid"], recent_list)))
        for raw_tx in recent_txids:
            data = gather_tx(rpc, raw_tx)
            recent.append(data)
    recent = sorted(recent, key=lambda r: r["rawtime"], reverse=True)
    context["recent"] = recent
    return b.template("address_recent", context)