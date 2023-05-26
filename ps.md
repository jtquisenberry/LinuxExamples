
```
ps -eo pid,ppid,nwchan,wchan:32,comm | grep ff
  123     2      1 rescuer_thread                   ata_sff
 1041     1 ffffff ep_poll                          systemd-timesyn
 1200     1 ffffff poll_schedule_timeout            vmtoolsd
 1262     1 ffffff poll_schedule_timeout            networkd-dispat
 1266     1 ffffff futex_wait_queue_me              ir_agent
 1364     1 ffffff poll_schedule_timeout            NetworkManager
 1376     1 ffffff futex_wait_queue_me              lxcfs
 1383     1 ffffff poll_schedule_timeout            rsyslogd
 1385     1 ffffff poll_schedule_timeout            irqbalance
 1403     1 ffffff poll_schedule_timeout            ModemManager
 1578  1509 ffffff futex_wait_queue_me              LSAgent
 1601     1 ffffff poll_schedule_timeout            polkitd
 2027     1 ffffff futex_wait_queue_me              dcservice
 2672     1 ffffff poll_schedule_timeout            accounts-daemon
 2735     1 ffffff poll_schedule_timeout            unattended-upgr
 3826  1266 ffffff futex_wait_queue_me              ir_agent
 4061  2027 ffffff futex_wait_queue_me              dcondemand
 4295  3826 ffffff poll_schedule_timeout            ir_agent
 4296  3826 ffffff poll_schedule_timeout            ir_agent
 6597     1 ffffff poll_schedule_timeout            packagekitd
17159  1266 ffffff futex_wait_queue_me              rapid7_endpoint
28134 28132 ffffff poll_schedule_timeout            python
28268  3826 ffffff poll_schedule_timeout            ir_agent
28552 28550 ffffff futex_wait_queue_me              python
28750 28552 ffffff futex_wait_queue_me              python
```


```
 ps -eo pid,ppid,nwchan,wchan:32,comm | grep futex
 1266     1 ffffff futex_wait_queue_me              ir_agent
 1376     1 ffffff futex_wait_queue_me              lxcfs
 1578  1509 ffffff futex_wait_queue_me              LSAgent
 2027     1 ffffff futex_wait_queue_me              dcservice
 3826  1266 ffffff futex_wait_queue_me              ir_agent
 4061  2027 ffffff futex_wait_queue_me              dcondemand
17159  1266 ffffff futex_wait_queue_me              rapid7_endpoint
28552 28550 ffffff futex_wait_queue_me              python
28750 28552 ffffff futex_wait_queue_me              python
```
