

```
# make
make -C /lib/modules/4.15.0-204-generic/build M=/home/myuser/git/LinuxExamples/kernel/addr modules
make[1]: Entering directory '/usr/src/linux-headers-4.15.0-204-generic'
  CC [M]  /home/myuser/git/LinuxExamples/kernel/addr/addr.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC      /home/myuser/git/LinuxExamples/kernel/addr/addr.mod.o
  LD [M]  /home/myuser/git/LinuxExamples/kernel/addr/addr.ko
make[1]: Leaving directory '/usr/src/linux-headers-4.15.0-204-generic'

```

```
# sudo insmod addr.ko
# dmesg | tail -5
[7754939.908488] Physical Address: &paddr 0x0000000ec57c4010
[7754939.912566] Physical Address: paddr ec57c4010
[7754939.916487] Virtual Address in Kernel: vaddr 0x00000000db83ac92
[7754939.920407] Virtual Address Value:  *((int*)vaddr) value 0x12345678
[7754939.924235] 0x78 0x56 0x34 0x12
# sudo rmmod addr
```
