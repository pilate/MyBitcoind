from bitcoinrpc.authproxy import AuthServiceProxy
from bitcoinrpc.authproxy import JSONRPCException
from socket import timeout
from socket import error


# Utility
def get_balance(rpc):
    unspent = rpc.listunspent(0)
    balance = sum(map(lambda u: u["amount"], unspent))
    return balance

def get_context():
    message = None
    try:
        rpc_connection = AuthServiceProxy("http://Pilate:password@127.0.0.1:8332", timeout=1)
        rpc_connection.getinfo()
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

    if rpc_connection:
        balance = get_balance(rpc_connection)
    else:
        balance = "Error"

    return {
        "balance": balance,
        "message": message,
        "rpc": rpc_connection
    }  
