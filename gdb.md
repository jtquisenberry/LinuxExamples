# Links

https://devguide.python.org/advanced-tools/gdb/

https://stackoverflow.com/questions/9573683/where-is-gdbinit-is-located-and-how-can-i-edit-it

https://www.podoliaka.org/2016/04/10/debugging-cpython-gdb/


# Add Python Dependencies

## Installs

```
apt-get install python3-dbg
```

## Within GDB

```
(gdb) source /usr/share/gdb/auto-load/usr/bin/python3.6-gdb.py
(gdb) source /usr/share/gdb/auto-load/usr/bin/python3.6-gdb_jq.py
```


## In Configuration

https://stackoverflow.com/questions/9573683/where-is-gdbinit-is-located-and-how-can-i-edit-it

```
nano ~/.gdbinit
```


