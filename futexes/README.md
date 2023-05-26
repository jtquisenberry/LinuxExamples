# Linux-examples

## View Processes with Futex

https://itecnote.com/tecnote/python-cant-enable-py-bt-for-gdb/


```
ps -eo pid,comm,ppid,wchan:32 | grep futex

root@mtpvpaslca07:/etc/filebeat# ps -eo pid,comm,ppid,wchan:32 | grep futex
  1122 lxcfs                1 futex_wait_queue_me
  1182 filebeat             1 futex_wait_queue_me
  1312 snapd                1 futex_wait_queue_me
 11430 python           11428 futex_wait_queue_me
 11605 python           11430 futex_wait_queue_me
 48333 dcservice            1 futex_wait_queue_me
 94135 dcondemand       48333 futex_wait_queue_me
```

## Install gdb

```
apt-get install gdb
apt-get install python3-dbg

```

## Run gdb

```
(gdb) source /usr/share/gdb/auto-load/usr/bin/python3.6-gdb.py
(gdb) info threads
(gdb) thread 1
(gdb) bt
(gdb) py-bt
(gdb) q
```

https://codeistry.wordpress.com/2016/10/24/gdb-find-the-thread-which-has-locked-the-mutex/






