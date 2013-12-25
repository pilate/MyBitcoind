import bottle as b


static_app = b.Bottle()


@static_app.get("/css/<filename:re:.*\.css>")
def static_css(filename):
    return b.static_file(filename, root="static/css")

@static_app.get("/js/<filename:re:.*\.js>")
def static_js(filename):
    return b.static_file(filename, root="static/js")