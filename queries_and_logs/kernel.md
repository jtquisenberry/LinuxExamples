
# Old Kernel Logs

```
# cd /var/log
# zcat dmesg.1.gz | grep "2025"
```


# journalctl
Although a bit late for the OP... 

I use Fedora, but if your system uses `journalctl` then you can easily get the kernel messages (dmesg log) from prior shutdown/crash (in a `dmesg -T` format) through the following.

**Options:**

 - -k (dmesg)
 - -b < *boot_number* > (How many reboots ago 0, -1, -2, etc.)
 - -o short-precise (dmesg -T)
 - -p *priority* Filter by priority output (4 to filter out notice and info).

NOTE: there is also an `-o short` and `-o short-iso` which gives you the date only, and the date-time in iso format respectively.

**Commands:**

 - All boot cycles  : `journalctl -o short-precise -k -b all`
 - Current boot     : `journalctl -o short-precise -k`
 - Last boot        : `journalctl -o short-precise -k -b -1`
 - Two boots prior  : `journalctl -o short-precise -k -b -2`
 - And so on

**Example Output:**

```
Feb 18 21:41:26.917400 localhost.localdomain kernel: usb 2-4: USB disconnect, device number 12
Feb 18 21:41:26.917678 localhost.localdomain kernel: usb 2-4.1: USB disconnect, device number 13
```

The amount of boots you can look back on can be viewed with the following.

 - `journalctl --list-boot`

The output of `journalctl --list-boot` looks like the following.

```
-2 6c29e3b6f6a14f549f06749f9710e1f2 Sat 2017-02-18 21:31:15 JST—Sat 2017-02-18 22:36:08 JST
-1 42fd465eacd345f7b595069c7a5a14d0 Sat 2017-02-18 22:51:22 JST—Sat 2017-02-18 23:08:30 JST  
 0 26ea10b064ce4559808509dc7f162f07 Sat 2017-02-18 23:09:25 JST—Sun 2017-02-19 00:57:35 JST
```

https://unix.stackexchange.com/questions/181067/how-to-read-dmesg-from-previous-session-dmesg-0 



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

