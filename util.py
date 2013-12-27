from bitcoinrpc.authproxy import AuthServiceProxy


# Utility
def get_balance(rpc):
    unspent = rpc.listunspent(0)
    balance = sum(map(lambda u: u["amount"], unspent))
    return balance

def get_context(rpc):
    message = None
    try:
        rpc.getinfo()
    except:
        balance = "Error"
        message = {
            "text": "Bitcoind connection error.",
            "type": "warning"
        }
    else:
        balance = get_balance(rpc)
        addresses = rpc.getaddressesbyaccount("")

    return {
        "balance": balance,
        "message": message,
        "addresses": addresses
    }  
