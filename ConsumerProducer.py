'''
Reference : https://www.agiliq.com/blog/2013/10/producer-consumer-problem-in-python/
'''


from threading import Thread
from queue import Queue
import time
import random

queue = Queue(10)

class ProducerThread(Thread):
    
    def run(self):
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            print("Producer has produced number {}".format(num))
            queue.put(num)
            time.sleep(random.random())


class ConsumerThread(Thread):
    def run(self):
        global queue

        while True:
            if not queue:
                print("Nothing in the queue, consumer is waiting")
                print("producer will add something to queue and will notify consumer")
            num = queue.get()
            queue.task_done()
            print("Consumer has Consumed number {}".format(num))
            time.sleep(random.random())


ProducerThread().start()
ConsumerThread().start()
