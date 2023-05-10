from multiprocessing import Process
from threading import Thread
from time import sleep
import os
import logging

def print_thread(ppid):
    placeholder = 1 
    i = 0
    while i < 2000:
    #while True:
        #placeholder += 1
        print("PRINT THREAD OF MAIN PROCESS PID:", ppid, flush=True)
        i += 1

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
