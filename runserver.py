from address_views import address_app
from import_views import import_app
from static_views import static_app

import bottle as b


# App Setup
app = b.default_app()

b.TEMPLATE_PATH.append("templates")
b.BaseTemplate.defaults['get_url'] = app.get_url

# View Setup
app.mount("/addresses/", address_app)
app.mount("/import/", import_app)
app.mount("/static/", static_app)

# Index
@app.get('/')
def index():
    out_obj = get_context()
    return b.template('index', out_obj)

app.run(host='loathes.asia', port=8080, debug=True, reloader=True)