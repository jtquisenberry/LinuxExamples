from threading import Thread
from multiprocessing import Process, set_start_method
import os
from time import sleep

def thread_printing(ppid):
  while True:
    print("abc", 9999999999999, ppid, flush=True)
    #sleep(.1)

def process_printing():
  print("CPID:", os.getpid())
  while True:
    print("def", 1111111111111, flush=True)



if __name__ == '__main__':
  set_start_method('spawn')
  print("PID:", os.getpid())
  threads = list()
  for i in range(1):
    thread = Thread(target=thread_printing, args=(os.getpid(),))
    threads.append(thread)

  for thread in threads:
    thread.start()

  process = Process(target=process_printing)
  process.start()
