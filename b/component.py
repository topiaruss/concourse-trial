import multiprocessing
from msgflow.api import Msgflow

print("starting B - cpu_count: %s" % multiprocessing.cpu_count())

flow = Msgflow({'bootstrap.servers':
                'winsome-hare-kafka.default.svc.cluster.local:9092'})
consumer = flow.get_consumer('testloop2')
try:
    while True:
        msg = consumer.get(timeout=0.1)
        if msg is None:
            continue
        else:
            print('Received message: {0}'.format(msg))
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
