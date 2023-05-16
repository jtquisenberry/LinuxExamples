from multiprocessing import Process
import multiprocessing
from threading import Thread
from time import sleep
import time
import datetime
import os
import sys
import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def print_thread(ppid):
    placeholder = 1 
    end = start = datetime.datetime.now() 
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    i = 0
    while i < 2000000000:
    #while True:
        #placeholder += 1
        print("PRINT THREAD OF MAIN PROCESS PID:", ppid, flush=True)
        #logger.info("PRINT THREAD OF MAIN PROCESS PID: {}".format(ppid))
        i += 1
    diff = (end - start).total_seconds()
    while diff < 1:
        # print(diff)
        end = datetime.datetime.now()
        diff = (end - start).total_seconds()
        sleep(0.5)
    children = multiprocessing.active_children()
    print(children)
    if children:
        print("CHILD PROCESS IS DEADLOCKED")
        for child in children:
            child.kill()
        sys.exit(0)
        sys.exit(0)
        os._exit(0)

def print_process():
    #sleep(120)
    cpid = os.getpid()
    path = './output/' + str(cpid) + '.txt'
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    #with open(path, 'w') as f:
        #f.write(str(cpid))
    #logger = logging.getLogger()
    #logging.basicConfig(level=logging.DEBUG)
    while True:
        #print("CPID:", cpid, flush=True)
        logger.info("CPID: {}".format(cpid))        
        break

if __name__ == '__main__':
    ppid = os.getpid()
    threads = list()
    for i in range(1):
        thread = Thread(target=print_thread, args=(ppid,))
    threads.append(thread)
    
    for thread in threads:
        thread.start()
    sleep(.1)
    process = Process(target=print_process)
    process.start()

    while True:
        if not multiprocessing.active_children():
            p = Process(target=print_process)
            p.start()
        sleep(0.1)

    print("DONE")
