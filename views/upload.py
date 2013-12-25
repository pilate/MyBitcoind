from bitcoinrpc.authproxy import JSONRPCException
from plugins import BitcoinRPCPlugin
from plugins import ContextPlugin


import bottle as b


upload_app = b.Bottle()
upload_app.install(BitcoinRPCPlugin())
upload_app.install(ContextPlugin())


@upload_app.get('/list/')
def import_list(rpc, context):
    context["privkeys"] = ""
    return b.template('import_list', context)

@upload_app.post('/list/')
def import_list(rpc, context):
    context["privkeys"] = ""
    form_addresses = b.request.forms.get("privkeys")
    split_addresses = form_addresses.split("\n");
    clean_list = map(str.strip, split_addresses)
    if rpc:
        added = 0
        for key in clean_list:
            try:
                rpc.importprivkey(key, "", False)
            except JSONRPCException:
                continue
            else:
                added += 1
        context["message"] = {
            "text": "Imported {0} new keys.".format(added),
            "type": "info"
        }
    else:
        context["privkeys"] = form_addresses
    return b.template('import_list', context)

@upload_app.get('/wallet/')
def import_wallet(rpc, context):
    return b.template('import_wallet', context)

@upload_app.post('/wallet/')
def import_wallet(rpc, context):
    post_file = b.request.files.get("file")
    file_data = post_file.file.read()
    return b.template('import_wallet', context)