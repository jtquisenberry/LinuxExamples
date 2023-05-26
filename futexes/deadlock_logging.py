from multiprocessing import Process
import multiprocessing
from threading import Thread
from time import sleep
import datetime
import os
import logging

def print_thread(ppid, logger):
    end = start = datetime.datetime.now() 
    i = 0
    while i < 3000000:
        #logger.info("PID: {}".format(ppid))
        #print("PRINT THREAD OF MAIN PROCESS PID:", ppid, flush=True)
        #sleep(0.001)
        i += 1
    #diff = (end - start).total_seconds()
    #print("Waiting 5 seconds for child process to terminate, if it will.")
    #while diff < 5:
    #    end = datetime.datetime.now()
    #    diff = (end - start).total_seconds()
    #    sleep(0.5)
    #children = multiprocessing.active_children()
    #print("Active Children:", children)
    #if children:
        #print("CHILD PROCESS IS DEADLOCKED")
        #for child in children:
        #    child.terminate()
        #os._exit(0)

def print_process(logger):
    placeholder = 0
    cpid = os.getpid()
    path = './output/' + str(cpid) + '.txt'
    with open(path, 'w') as f:
        f.write(str(cpid))
    while True:
        logger.info("CPID: {}".format(cpid))        

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    logging.basicConfig(level=logging.DEBUG)
    ppid = os.getpid()
    threads = list()
    logger = logging.getLogger()
    logger.setLevel('INFO')
    for i in range(1):
        thread = Thread(target=print_thread, args=(ppid, logger))
    threads.append(thread)
    
    for thread in threads:
        thread.start()

    process = Process(target=print_process, args=(logger,))
    process.start()
    print("DONE")
