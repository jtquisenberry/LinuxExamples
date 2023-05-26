# Links

https://askubuntu.com/questions/532329/how-do-i-find-a-recent-file-by-date-created

https://www.abelworld.com/ctime-mtime-atime-find-command/

Ok so we got a command now you should know the main parameters and be able to find help if needed:

    ctime is creation time in days.
    mtime is modification time in days.
    atime is access time in days.
    cmin same as -ctime, but in minutes
    mmin same as -mtime but in minutes
    amin same as -atime but in days.

Find has many other parameters that help you filter by other many parameters, you can just execute man and check them out or make s simple search in google. Another thing you need to keep present is the sign of the integer number, e.g.:

    mtime -3 means younger than 3+1 days.
    atime 5 means exactly between 5 and 6 days.
    ctime +4 means older than 4+1 days.
    Then you can combine statements like ‘-ctime +2 -ctime -4’ which means between those two numbers (remember the +1 so it would be between 3 and 5).


# Examples

```
find -name stap
find -name systemtap
find -ctime -.1
find -ctime -2
find -type d -ctime -1
find /usr/share/gdb/auto-load/usr/bin/ -name python*
find . -name "foo*"
```

