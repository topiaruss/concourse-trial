import datetime
import multiprocessing
import time
from msgflow.api import Msgflow

print("starting A - cpu_count: %s" % multiprocessing.cpu_count())

flow = Msgflow({'bootstrap.servers':
                'winsome-hare-kafka.default.svc.cluster.local:9092'})
while 1:
    for bits in range(19):
        start_level_at = time.time()
        end_at = start_level_at + 20.0
        wait = 1.0 / (1 << bits)
        print(bits, wait)
        century = 0
        while time.time() < end_at:
            msg = dict(hello='world %s at %s' %
                      (wait, datetime.datetime.now()))
            flow.put('testloop3', msg)
            time.sleep(wait)
            century += 1
            if century == 100:
                century = 0
                flow.flush()

    print('flush bits %s msg %s' % (bits, msg))
    flow.flush()

