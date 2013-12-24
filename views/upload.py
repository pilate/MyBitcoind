from plugins import BitcoinRPCPlugin
from util import get_context

import bottle as b


upload_app = b.Bottle()
upload_app.install(BitcoinRPCPlugin())


@upload_app.get('/list/')
def import_list(rpc):
    out_obj = get_context(rpc)
    out_obj["privkeys"] = ""
    return b.template('import_list', out_obj)

@upload_app.post('/list/')
def import_list(rpc):
    out_obj = get_context(rpc)
    out_obj["privkeys"] = ""
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