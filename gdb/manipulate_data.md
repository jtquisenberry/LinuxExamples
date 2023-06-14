# Manipulate Data
-------------

# Thread

Ask current thread to exit gracefully. 

```
(gdb) call pthread_exit(0)

```


# Semaphore

```
(gdb) set var *0x7fbdd42baef0 = 0
(gdb) p *(int *)0x7fbdd42baef0
$13 = 0
(gdb) p sem_getvalue((*(SemLockObject *)0x7fbe02820c00).handle, 0x7fbdd42baef0)
$14 = 0
(gdb) p *(int *)0x7fbdd42baef0
$15 = 6

```

is equivalent to 

```
tasks._unfinished_tasks._semlock._get_value()

```

Note that the number of items in the queue may be different from the number of incomplete tasks.

```
>>> # incomplete tasks
>>> tasks._unfinished_tasks._semlock._get_value()
2
```

```
>>> # items in the queue
>>> tasks.qsize()
1
>>> # Another way to get items in the queue
>>> tasks._maxsize - tasks._sem._semlock._get_value()
>>> # = 3000 - 2999
1

```
