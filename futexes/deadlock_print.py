from multiprocessing import Process, set_start_method
from threading import Thread
from time import sleep
import os

def print_thread(pid):
    placeholder = 1 
    while True:
        print("PRINT THREAD OF MAIN PROCESS PID:", pid, flush=True)

def print_process():
    cpid = os.getpid()
    #path = './output/' + str(cpid) + '.txt'
    #with open(path, 'w') as f:
    #    f.write(str(cpid))
    while True:
        print("CPID:", cpid, flush=True)

if __name__ == '__main__':
    #set_start_method('spawn', force=True)
    pid = os.getpid()
    threads = list()
    for i in range(1):
        thread = Thread(target=print_thread, args=(pid,))
    threads.append(thread)
    
    for thread in threads:
        thread.start()

    process = Process(target=print_process)
    process.start()
