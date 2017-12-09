import concurrent.futures
import multiprocessing
import time
import datetime

from msgflow.component import Component, Msgflow
from py_zipkin.zipkin import zipkin_client_span

print("starting Gamma - cpu_count: %s" % multiprocessing.cpu_count())


class Gamma(Component):
    def __init__(self, topic):
        super().__init__(topic, pre_drain=True)

    def process_one(self, zipkin_context, data):
        self.sub1()

    @zipkin_client_span(service_name='Gamma', span_name='sub1')
    def sub1(self):
        self.zipkin_context.update_binary_annotations(dict(
            winter='in the rain',
            zdict=dict(a=1,b=2,c='see')
        ))
        time.sleep(0.02)


g = Gamma('gamma_topic')
g.run()
