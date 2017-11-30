import datetime
import multiprocessing
import time
from msgflow.api import Msgflow

print("starting A - cpu_count: %s" % multiprocessing.cpu_count())

flow = Msgflow({'bootstrap.servers': 'kafka:9092'})

# tested with MAXBITS 19, single partition kafka on spinning drive.
# borderline stable.
# Pulled it back to 8 while testing other features.
MAX_BIT_SHIFTS = 8

while 1:
    for bits in range(MAX_BIT_SHIFTS):
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
            if century == 500:
                century = 0
                flow.flush()

    print('flush bits %s msg %s' % (bits, msg))
    flow.flush()

