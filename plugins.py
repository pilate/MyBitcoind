from bitcoinrpc.authproxy import AuthServiceProxy
from bottle import PluginError

import inspect
import settings


class ContextPlugin(object):
    api = 2
    keyword = "context"
    name = "context"

    def setup(self, app):
        for other in app.plugins:
            if not isinstance(other, ContextPlugin): continue
            if other.keyword == self.keyword:
                raise PluginError("Found conflicting context plugin.")

    def apply(self, callback, route):
        args = inspect.getargspec(route.callback)[0]
        if (self.keyword not in args) or ("rpc" not in args):
            return callback

        def wrapper(*args, **kwargs):
            kwargs[self.keyword] = get_context(kwargs["rpc"])
            rv = callback(*args, **kwargs)
            return rv

        return wrapper

class BitcoinRPCPlugin(object):
    api = 2
    keyword = "rpc"
    name = "bitcoinrpc"
    
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
