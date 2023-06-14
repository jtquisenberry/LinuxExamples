# Manipulate Data
-------------

# Thread

Ask current thread to exit gracefully. 

```
(gdb) call pthread_exit(0)

```


# Semaphore

Use `py-fields` to get the addresses of the `_sem` and `_unfinished_tasks` members of a `JoinableQueue`. In this example, the `JoinableQueue` `tasks` variable is not local and not available to `py-fields`. However, `w` is a `Process` to which `tasks` was passed as `task_queue`. `Process` `w` is local and available to `py-fields`.

```
(gdb) frame 13
(gdb) /<path>/pyfields.py
#13 0x0000000000509b39 in PyEval_EvalFrameEx (throwflag=0,
    f=Frame 0x7f197c06d8c8, for file /usr/lib/python3.6/multiprocessing/queues.py, line 305, in join (self=<JoinableQueue(_maxsize=3000, ...
(gdb) py-fields w.task_queue._unfinished_tasks
local '_unfinished_tasks' = <Semaphore(_semlock=<_multiprocessing.SemLock at remote 0x7f19467618f0>, acquire=<built-in method acquire of _multiprocessing.SemLock object at remote 0x7f19467618f0>, release=<built-in method release of _multiprocessing.SemLock object at remote 0x7f19467618f0>) at remote 0x7f1946761a20>
(gdb) py-fields w.task_queue._sem
local '_sem' = <BoundedSemaphore(_semlock=<_multiprocessing.SemLock at remote 0x7f19467616c0>, acquire=<built-in method acquire of _multiprocessing.SemLock object at remote 0x7f19467616c0>, release=<built-in method release of _multiprocessing.SemLock object at remote 0x7f19467616c0>) at remote 0x7f1946761898>
```

Identify a region of memory that `gdb` has write access to. If a variable in the stack is at an address and the value does not need to be preserved, the the address of the variable is a good choice. Suppose there is a `futex` that needs to be unlocked; the address of its `futex_word` is a good choice. 

```
(gdb) bt
#0  0x00007f1a24a7b7c6 in futex_abstimed_wait_cancelable (private=128, abstime=0x0, expected=0, futex_word=0x7f1a250a5000) at ../sysdeps/unix/sysv/linux/futex-internal.h:205
```

If the value to be written to is not already an `int`, write an `int` to it.

```
(gdb) set var *0x7f1a250a5000 = 0
(gdb) p *(int *)0x7f1a250a5000
$13 = 0
```

Call `sem_getvalue(SemLockObject.handle, output address)` on `_unfinished_tasks`. This is equivalent to the Python code:

```
>>> # Get unfinished tasks
>>> tasks._unfinished_tasks._semlock._get_value()
```

```
(gdb) p sem_getvalue((*(SemLockObject *)0x7f1946761a20).handle, 0x7f1a250a5000)
$14 = 0
(gdb) p *(int *)0x7f1a250a5000
$15 = 6
```

Call `sem_getvalue(SemLockObject.handle, output address)` on `_unfinished_tasks`. This is equivalent to the Python code:

```
??????????
```

```
(gdb) p sem_getvalue((*(SemLockObject *)0x7f1946761898).handle, 0x7f1a250a5000)
$14 = 0
(gdb) p *(int *)0x7f1a250a5000
$15 = 0
```



Python

```
>>> # items in the queue
>>> tasks.qsize()
1
>>> # Another way to get items in the queue
>>> tasks._maxsize - tasks._sem._semlock._get_value()
>>> # = 3000 - 2999
1

```
