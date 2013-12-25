from bitcoinrpc.authproxy import AuthServiceProxy
from socket import timeout
from socket import error


# Utility
def get_balance(rpc):
    unspent = rpc.listunspent(0)
    balance = sum(map(lambda u: u["amount"], unspent))
    return balance

def get_context(rpc):
    message = None
    try:
        rpc.getinfo()
    except timeout:
        rpc_connection = None
        message = {
            "text": "Bitcoind connection timeout.",
            "type": "warning"
        }
    except error:
        rpc_connection = None
        message = {
            "text": "Bitcoind connection refused.",
            "type": "warning"
        }

    if rpc:
        balance = get_balance(rpc)
    else:
        balance = "Error"

    return {
        "balance": balance,
        "message": message,
        "rpc": rpc
    }  
