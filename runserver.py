from views.static import static_app
from views.address import address_app
from views.upload import upload_app

from plugins import BitcoinRPCPlugin
from util import get_context

import bottle as b


# App Setup
app = b.default_app()
app.install(BitcoinRPCPlugin())

b.TEMPLATE_PATH.append("templates")
b.BaseTemplate.defaults['get_url'] = app.get_url

# Views Setup
app.mount("/addresses/", address_app)
app.mount("/import/", upload_app)
app.mount("/static/", static_app)

@app.get('/')
def index(rpc):
    out_obj = get_context(rpc)
    return b.template('index', out_obj)

app.run(host='loathes.asia', port=8080, debug=True, reloader=True)