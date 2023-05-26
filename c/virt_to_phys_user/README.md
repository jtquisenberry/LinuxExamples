Program `virt_to_phys_user` translates a memory address in a process's virtual address space to a memory address in physical memory. 

Program `test_program` prints its PID and the address of a variable whose address is 0x12345678. It sleeps after printing so that there is time to examine the process's memory. 

# Build and Permissions

```
# gcc virt_to_phys_user.c -o virt_to_phys_user.o
# gcc test_program.c -o test_program.o
# chmod +x virt_to_phys_user.o
# chmod +x test_program.o
```


# Usage

Get the PID of a process and the virtual address of a symbol (variable) within the process.

```
# ./test_program.o
vaddr 0x562c4ba8f010
pid 129608
```

Get the physical address corresponding to the virtual address.

```
# ./virt_to_phys_user.o 129608 0x562c4ba8f010
0xfdcf80010
```


# Links

https://github.com/cirosantilli/linux-kernel-module-cheat/blob/master/userland/linux/virt_to_phys_user.c

https://stackoverflow.com/questions/5748492/is-there-any-api-for-determining-the-physical-address-from-virtual-address-in-li/45128487#45128487
