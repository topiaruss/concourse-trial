import concurrent.futures
import multiprocessing
import time
import datetime

from msgflow.component import Component, Msgflow
from py_zipkin.zipkin import zipkin_client_span

print("starting Gamma - cpu_count: %s" % multiprocessing.cpu_count())


class Gamma(Component):
    def __init__(self, topic, offset="largest"):
        super().__init__(topic, offset=offset)

    def process_one(self, zipkin_context, data):
        self.sub1()

    @zipkin_client_span(service_name='Gamma', span_name='sub1')
    def sub1(self):
        time.sleep(0.02)


g = Gamma('gamma_topic', offset="largest")
g.run()
