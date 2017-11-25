"""Experimental concurrency for supertask"""
import concurrent.futures
import time
from bottle import Bottle


class EndpointServer(Bottle):
    def __init__(self):
        super(EndpointServer, self).__init__()
        self.route('/live', callback=self.live)
        self.route('/ready', callback=self.ready)

    def live(self):
        return "Hello, I'm live\n"

    def ready(self):
        return "Hello, I'm ready\n"


def pend():
    while 1:
        print(".", end='', flush=True)
        time.sleep(1.0)


def live():
    app = EndpointServer()
    app.run(host='localhost', port=8000)


def run():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Start the load operations and mark each future with its URL
        plive = executor.submit(live)
        pfuture = executor.submit(pend)


if __name__ == "__main__":
    run()