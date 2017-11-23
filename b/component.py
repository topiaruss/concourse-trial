import multiprocessing
from msgflow.api import Msgflow

print("starting B - cpu_count: %s" % multiprocessing.cpu_count())

flow = Msgflow({'bootstrap.servers':
                'winsome-hare-kafka.default.svc.cluster.local:9092'})
consumer = flow.get_consumer('testloop3')
try:
    count = 0
    while True:
        msg = consumer.get(timeout=0.1)
        if msg is None:
            continue
        else:
            if count == 0:
                print('Received message: {0}'.format(msg))
            count += 1
            count = count % 512
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
