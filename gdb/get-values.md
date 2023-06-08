# Get Values

## Semaphore

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
