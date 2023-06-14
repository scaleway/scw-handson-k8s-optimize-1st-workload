#!/usr/local/bin/python

import bottle, socket, functools, os, random, math
from multiprocessing import Process

print = functools.partial(print, flush=True)

def base_app():
    base_app = bottle.Bottle()
    
    @base_app.route("/")
    def root():
        base = f"""Hello! My name is <b>{socket.gethostname()}</b><br/><br/>
Here is the value of ENV_CONFIG <b>{os.getenv('ENV_CONFIG',default='undefined')}</b><br/>
Here is the value of ENV_SECRET <b>{os.getenv('ENV_SECRET',default='undefined')}</b>"""

        # generate load, based on registry.k8s.io/hpa-example but in python instead of php
        x = 0.0001
        for i in range(1000000):
            x += math.sqrt(x)

        return base
    
    base_app.run(host="0.0.0.0", port=80, server="paste")

def metrics_app():
    metrics_app = bottle.Bottle()

    @metrics_app.route("/")
    def root():
        metrics = f"""# HELP myapp_test_metric Random number between 0 and 100
# TYPE myapp_test_metric gauge
myapp_test_metric {random.randint(0, 100)}.0"""
        return metrics

    metrics_app.run(host="0.0.0.0", port=9001, server="paste")

if __name__ == "__main__":
    ps = []
    for f in [base_app, metrics_app]:
        ps.append(Process(target=f))
    for p in ps:
        p.start()
    for p in ps:
        p.join()
