# Filesystem

https://unix.stackexchange.com/questions/356292/monitor-disk-writes-by-directory

# Installation
```
$ apt install inotify-tools
$ apt install fatrace
```
 
# Use
File Accesses to `/opt/mydir`
```
inotifywait -m -r /opt/mydir
fatrace | grep "opt/mydir"
```

File Writes to `/opt/mydir`
``` 
inotifywait -m -r -e modify /opt/mydir
fatrace -f W | grep "opt/mydir"
```
