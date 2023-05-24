from multiprocessing import Process
import multiprocessing
from threading import Thread
from time import sleep
import datetime
import os
import sys
import logging

def print_thread(ppid):
    end = start = datetime.datetime.now() 
    i = 0
    while i < 3000:
        print("PRINT THREAD OF MAIN PROCESS PID:", ppid, flush=True)
        # sleep(0.001)  # Shorter sleep times increase the probability of deadlock.
        i += 1
    diff = (end - start).total_seconds()
    print("Waiting 5 seconds to allow child process to terminate if it will.")
    while diff < 5:
        end = datetime.datetime.now()
        diff = (end - start).total_seconds()
        sleep(0.5)
    children = multiprocessing.active_children()
    print("Active Children:", children)
    if children:
        print("CHILD PROCESS IS DEADLOCKED")
        for child in children:
            child.terminate()
        sys.exit(0)
    else:
        print("Child process is NOT deadlocked")

def print_process():
    placeholder = 0

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
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
