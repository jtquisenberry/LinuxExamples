from multiprocessing import Process
from threading import Thread
from time import sleep
import os

def print_thread(ppid):
    placeholder = 1 
    while True:
        #placeholder += 1
        print("PRINT THREAD OF MAIN PROCESS PID:", ppid, flush=True)

def print_process():
    #sleep(120)
    cpid = os.getpid()
    #path = '/home/jquisenberry/python/out.txt'
    path = './' + str(cpid) + '.txt'
    with open(path, 'w') as f:
        f.write(str(cpid))
    while True:
        print("CPID:", cpid, flush=True)

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
