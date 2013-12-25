from bitcoinrpc.authproxy import AuthServiceProxy
from bottle import PluginError

import inspect


class BitcoinRPCPlugin(object):
    name = "bitcoinrpc"
    keyword = "rpc"
    api = 2

    def __init__(self):
        pass

    def setup(self, app):
        for other in app.plugins:
            if not isinstance(other, BitcoinRPCPlugin): continue
            if other.keyword == self.keyword:
                raise PluginError("Found conflicting bitcoinrpc plugin.")

    def apply(self, callback, route):
        args = inspect.getargspec(route.callback)[0]
        if self.keyword not in args:
            return callback

        def wrapper(*args, **kwargs):
            print "Wrapper apply"
            kwargs[self.keyword] = AuthServiceProxy("http://Pilate:password@127.0.0.1:8332")
            rv = callback(*args, **kwargs)
            return rv

        return wrapper
