#!/usr/local/bin/python

import bottle, socket, functools, os

print = functools.partial(print, flush=True)
app = bottle.Bottle()

@app.route("/")
def root():
    return f"Hello! My name is <b>{socket.gethostname()}</b><br/><br/>I'm currently running in namespace <b>{os.getenv('K8S_NS', default='undefined')}</b> on node <b>{os.getenv('K8S_NODE', default='undefined')}</b>\n"

app.run(host="0.0.0.0", port=80, server="paste")
