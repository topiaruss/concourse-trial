import datetime
import multiprocessing
import time
from msgflow.api import Msgflow

print("starting A - cpu_count: %s" % multiprocessing.cpu_count())

flow = Msgflow({'bootstrap.servers':
                'winsome-hare-kafka.default.svc.cluster.local:9092'})
while 1:
    for bits in range(14):
        start_level_at = time.time()
        end_at = start_level_at + 30.0
        wait = 1.0 / (1 << bits)
        while time.time() < end_at:
            msg = dict(hello='world %s at %s' %
                      (wait, datetime.datetime.now()))
            flow.put('testloop3', msg)
            time.sleep(wait)

    print('flush bits %s msg %s' % (bits, msg))
    flow.flush()

