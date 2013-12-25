from bitcoinrpc.authproxy import AuthServiceProxy
from bottle import PluginError

import inspect
import settings


class BitcoinRPCPlugin(object):
    name = "bitcoinrpc"
    keyword = "rpc"
    api = 2

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
            kwargs[self.keyword] = AuthServiceProxy(settings.rpc_connect)
            rv = callback(*args, **kwargs)
            kwargs[self.keyword]._AuthServiceProxy__conn.close()
            return rv

        return wrapper
