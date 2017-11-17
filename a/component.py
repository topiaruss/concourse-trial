from confluent_kafka import Producer
import time
import datetime

print("starting A")
p = Producer({'bootstrap.servers': 'winsome-hare-kafka:9092'})
while 1:
    for i in range(10):
        mess = 'world %s' % datetime.datetime.now()
        p.produce('testloop', key='hello', value=mess)
    time.sleep(1)
    print('flush ' + mess)
    p.flush()
