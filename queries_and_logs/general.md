
# Old Kernel Logs

```
# cd /var/log
# zcat dmesg.1.gz | grep "2025"
```



# Kernel Logs Timestamps

Manually convert the timestamp. 

The timestamp in `dmesg` is the offset in seconds since last reboot so : 


1. Determine the last reboot:  

        
        [root@server ~]# last -n 1 reboot
        reboot   system boot  3.10.0-1160.76.1 Sat Aug 27 10:56 - 14:25 (29+03:28)
        
        wtmp begins Tue Nov  7 09:30:18 2017 


2.   For example my ` dmesg` has an entry:   
  
         [2316645.206965] BIOS EDD facility v0.16 2004-Jun-25, 1 devices found

https://serverfault.com/questions/1111513/dmesg-to-real-timestamp

