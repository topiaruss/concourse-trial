from confluent_kafka import Producer
import datetime
import multiprocessing
import time
from msgflow.api import Msgflow

print("starting A - cpu_count: %s" % multiprocessing.cpu_count())

flow = Msgflow({'bootstrap.servers':
                'winsome-hare-kafka.default.svc.cluster.local:9092'})
while 1:
    for i in range(10):
        msg = dict(hello='world at %s' % datetime.datetime.now())
        flow.put('testloop2', msg)
    print('flush %s' % msg)
    flow.flush()
    time.sleep(1)

