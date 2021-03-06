import multiprocessing
import time

from msgflow.component import Component, Msgflow
from py_zipkin.zipkin import zipkin_span

print("starting Beta - cpu_count: %s" % multiprocessing.cpu_count())


class Beta(Component):
    def __init__(self, topic):
        super().__init__(topic, pre_drain=True)

    def process_one(self, zipkin_context, data):
        self.zipkin_context = zipkin_context
        self.sub1()
        self.enqueue_item(zipkin_context, 'gamma_topic', dict(gamma=3))
        self.enqueue_item(zipkin_context, 'gamma_topic', dict(gamma=4))
        time.sleep(0.02)
        self.sub1()

    @zipkin_span(service_name='Beta', span_name='sub1')
    def sub1(self):
        self.zipkin_context.update_binary_annotations(dict(
            autumn='in the shade'))
        time.sleep(0.05)


b = Beta('beta_topic')
b.run()
