from views.static import static_app
from views.address import address_app
from views.upload import upload_app

from plugins import BitcoinRPCPlugin
from plugins import ContextPlugin
from util import get_context

import bottle as b


# App Setup
app = b.default_app()
app.install(BitcoinRPCPlugin())
app.install(ContextPlugin())

b.TEMPLATE_PATH.append("templates")
b.BaseTemplate.defaults["get_url"] = app.get_url

# Views Setup
app.mount("/addresses/", address_app)
app.mount("/import/", upload_app)
app.mount("/static/", static_app)

@app.get("/")
def index(rpc, context):
    if rpc:
        context["address_count"] = len(rpc.getaddressesbyaccount(""))
        context["unspent_outputs"] = len(rpc.listunspent(0))
        received_addresses = rpc.listreceivedbyaddress(0)
        context["total_received"] = sum(map(lambda r: r["amount"], received_addresses))
    return b.template("index", context)

app.run(host="0.0.0.0", port=8080, debug=True, reloader=True)