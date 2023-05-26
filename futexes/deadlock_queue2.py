import multiprocessing
from multiprocessing import Process, JoinableQueue
from threading import Thread
import logging
import datetime
import time

def do_work(q):
    while True:
        num = q.get()
        #if num is None:
        if num % 400 == 0:
            q.task_done()
            break
        #if num == 1:
        #    time.sleep(5000)
        #logging.error(num)
        q.task_done()

def do_work_t(q):
    while True:
        num = q.get()
        #logging.error(num)
        q.task_done()



if __name__ == '__main__':
    q = JoinableQueue()

    process_count = 400
    for i in range(1, process_count * 400+1):
        q.put(i)

    t = Thread(target=do_work_t, args=(q,))
    t.start()



    #for i in range(process_count):
    #    q.put(None)

    processes = list()
    for i in range(process_count):
        p = Process(target=do_work, args=(q,))
        processes.append(p)

    for p in processes:
        p.start()
        #time.sleep(.1)

    #for i in range(1000, 2000):
    #    q.put(i)

    #for p in processes:
    #    q.put(None)

    q.join()

    print("DONE")
