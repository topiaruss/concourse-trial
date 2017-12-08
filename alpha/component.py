import concurrent.futures
import datetime
import time

from msgflow.component import Component, Msgflow
from py_zipkin.zipkin import zipkin_client_span


class Alpha(Component):
    def __init__(self, topic):
        super().__init__(topic, pre_drain=True)

    def process_one(self, zipkin_context, data):
        #self.logger.debug('TRIGGER CHAIN %s' % data)
        zipkin_context.update_binary_annotations(dict(foo='bar'))
        self.sub1()
        self.enqueue_item(zipkin_context, 'beta_topic', dict(beta=2))
        self.sub2()

    @zipkin_client_span(service_name='Alpha', span_name='sub1')
    def sub1(self):
        time.sleep(0.01)
        self.sub1sub1()
        time.sleep(0.03)
        self.sub1sub2()

    @zipkin_client_span(service_name='Alpha', span_name='sub1.sub1')
    def sub1sub1(self):
        time.sleep(0.02)

    @zipkin_client_span(service_name='Alpha', span_name='sub1.sub2')
    def sub1sub2(self):
        time.sleep(0.02)

    @zipkin_client_span(service_name='Alpha', span_name='sub2')
    def sub2(self):
        time.sleep(0.03)
        raise ValueError('Dummy exception')


a = Alpha('alpha_topic')
flow = Msgflow({'bootstrap.servers': 'kafka:9092'})


def initiate_sample_tasks():
    """loop that posts on the alpha topic regularly"""
    time.sleep(0.25)
    # logger = logging.getLogger('Putter')
    while True:
        flow.put('alpha_topic', dict(a=0, time=str(datetime.datetime.now())))
        time.sleep(5.0)


# only adding this so we can have concurrent put tasks, for testing.
tasks = [a.run, initiate_sample_tasks]
with concurrent.futures.ThreadPoolExecutor(
        max_workers=len(tasks)) as executor:
    for t in tasks:
        executor.submit(t)
