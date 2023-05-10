from multiprocessing import Process
import multiprocessing
from threading import Thread
from time import sleep
import time
import datetime
import os
import sys
import logging

def print_thread(ppid):
    placeholder = 1 
    end = start = datetime.datetime.now() 
    i = 0
    while i < 2000:
    #while True:
        #placeholder += 1
        print("PRINT THREAD OF MAIN PROCESS PID:", ppid, flush=True)
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
    #with open(path, 'w') as f:
        #f.write(str(cpid))
    #logger = logging.getLogger()
    #while True:
        #print("CPID:", cpid, flush=True)
        #logger.warning("CPID: {}".format(cpid))        

if __name__ == '__main__':
    ppid = os.getpid()
    threads = list()
    for i in range(1):
        thread = Thread(target=print_thread, args=(ppid,))
    threads.append(thread)
    
    for thread in threads:
        thread.start()

    process = Process(target=print_process)
    process.start()
    print("DONE")
