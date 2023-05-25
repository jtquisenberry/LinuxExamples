```
sudo strace -p 117991
```


```
sudo strace -k -p 117991
```
 
 
 


```
$ cat /proc/<PID>/stack
[<ffffffff81012b72>] save_stack_trace_tsk+0x22/0x40
[<ffffffff81213abe>] proc_pid_stack+0x8e/0xe0
[<ffffffff81214960>] proc_single_show+0x50/0x90
[<ffffffff811cd970>] seq_read+0xe0/0x3e0
[<ffffffff811a6a84>] vfs_read+0x94/0x180
[<ffffffff811a7729>] SyS_read+0x49/0xb0
[<ffffffff81623ad2>] system_call_fastpath+0x16/0x1b
[<ffffffffffffffff>] 0xffffffffffffffff
```
