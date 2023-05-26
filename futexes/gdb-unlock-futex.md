# Unlock a Futex

## Start gdb

GDB attached to the process and put it in a paused state.

```
sudo gdb -p 95348
```

## Set a Catchpoint and Continue Execution

A catchpoint is a breakpoint that breaks whenever the specified system call is made. In the x64 architecture, `FUTEX` is 202. See [Set Catchpoint][1], [Syscalls][2]

```
(gdb) catch syscall 202
Catchpoint 1 (syscall 'futex' [202])
(gdb) continue
Continuing.
```

## View Threads

Both child threads are blocked at a `futex`.

```
(gdb) info threads
  Id   Target Id         Frame
  1    Thread 0x7f7e797e0740 (LWP 95348) "python3" 0x00007f7e78fc87c6 in futex_abstimed_wait_cancelable (private=0, abstime=0x0, expected=0, futex_word=0x7f7e70000e70) at ../sysdeps/unix/sysv/linux/futex-internal.h:205
* 2    Thread 0x7f7e7811e700 (LWP 95349) "python3" 0x00007f7e78fc87c6 in futex_abstimed_wait_cancelable (private=0, abstime=0x0, expected=0, futex_word=0x1621fc0) at ../sysdeps/unix/sysv/linux/futex-internal.h:205
  3    Thread 0x7f7e7791d700 (LWP 95350) "python3" 0x00007f7e78fc87c6 in futex_abstimed_wait_cancelable (private=0, abstime=0x0, expected=0, futex_word=0x1621f90) at ../sysdeps/unix/sysv/linux/futex-internal.h:205
```

## Access One Thread

```
(gdb) thread 2
[Switching to thread 2 (Thread 0x7f7e7811e700 (LWP 95349))]
#0  0x00007f7e78fc87c6 in futex_abstimed_wait_cancelable (private=0, abstime=0x0, expected=0, futex_word=0x1621fc0) at ../sysdeps/unix/sysv/linux/futex-internal.h:205
```

## Get, Set, and Get the Value at the Address of the Futex

`0` is locked, and `1` is unlocked. For information about assignment, see [Assignment][3]

```
(gdb) print futex_word
$1 = (unsigned int *) 0x1621fc0
(gdb) print *(unsigned int *) 0x1621fc0
$2 = 0
(gdb) set var *(unsigned int *) 0x1621fc0 = 1
(gdb) print *(unsigned int *) 0x1621fc0
$3 = 1
```

## Remove Catchpoint and Continue

```
(gdb) info breakpoints
Num     Type           Disp Enb Address            What
1       catchpoint     keep y                      syscall "futex"
        catchpoint already hit 37 times
(gdb) delete 1
(gdb) continue
Continuing.
```

## Application Prints Messages with Exceptions

```
Thread thread1 before acquire lock1
Thread thread1 acquired lock1
Thread thread2 before acquire lock2
Thread thread2 acquired lock2
Thread thread1 before acquire lock2
Thread thread2 before acquire lock1
Thread thread1 DEADLOCK: This line will never run.
Thread thread2 DEADLOCK: This line will never run.
Exception in thread Thread-2:
Traceback (most recent call last):
  File "m5.py", line 25, in func2
    print('Thread',name,'DEADLOCK: This line will never run.')
RuntimeError: release unlocked lock

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3.6/threading.py", line 916, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.6/threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "m5.py", line 25, in func2
    print('Thread',name,'DEADLOCK: This line will never run.')
RuntimeError: release unlocked lock

```

## Threads Exit

```
[Thread 0x7f7e7791d700 (LWP 95350) exited]
[Thread 0x7f7e7811e700 (LWP 95349) exited]
[Inferior 1 (process 95348) exited normally]
```


  [1]: https://sourceware.org/gdb/onlinedocs/gdb/Set-Catchpoints.html
  [2]: https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md
  [3]: https://sourceware.org/gdb/download/onlinedocs/gdb/Assignment.html
