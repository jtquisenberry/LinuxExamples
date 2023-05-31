# System

* Ubuntu 22.04
* Kernel 5.19.0-42-generic vmlinux

# Introduction

Debugging a kernel or a kernel module modules with GDB is typically not done one the machine running the code. Instead, the kernel is run in a virtual machine (the guest system), often a QEMU virtual machine. The debugger is attached in the host system. 

I performed the steps described in this document to setup a guest machine running.

# Ensure the kernel was configured with the required options.

```
/boot/# nano config-5.19.0-42-generic
```

## For kgdb

```
# CONFIG_STRICT_KERNEL_RWX is not set
CONFIG_FRAME_POINTER=y
CONFIG_KGDB=y
CONFIG_KGDB_SERIAL_CONSOLE=y
```

## For kdb

```
# CONFIG_STRICT_KERNEL_RWX is not set
CONFIG_FRAME_POINTER=y
CONFIG_KGDB=y
CONFIG_KGDB_SERIAL_CONSOLE=y
CONFIG_KGDB_KDB=y
CONFIG_KDB_KEYBOARD=y

```

If I were trying to replace the current kernel, I would follow the procedure described here: https://phoenixnap.com/kb/build-linux-kernel .

Identify Kernel Version

```
# uname -r
5.19.0-42-generic
```


Install Linux Headers

```
sudo apt-get install -y linux-headers-`uname -r`
```
Notice that this command incorporates `uname -r`, which provides the kernel version. 

```


Install vmlinux

Reference: http://superuser.com/questions/62575/where-is-vmlinux-on-my-ubuntu-installation

vmlinux is required to provide kernel symbols to gdb.

```

echo "deb http://ddebs.ubuntu.com $(lsb_release -cs)-updates main restricted universe multiverse
deb http://ddebs.ubuntu.com $(lsb_release -cs)-security main restricted universe multiverse
deb http://ddebs.ubuntu.com $(lsb_release -cs)-proposed main restricted universe multiverse" | \
sudo tee -a /etc/apt/sources.list.d/ddebs.list

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 428D7C01

sudo apt-get update
sudo apt-get install linux-image-$(uname -r)-dbgsym
```

My system contains vmlinux files at `/usr/lib/debug/boot/`.

Copy the file whose version most closely matches the kernel version to `vmlinux`.

```
# cd /usr/lib/debug/boot
# ls
vmlinux-5.19.0-41-generic  vmlinux-5.19.0-42-generic
# cp vmlinux-5.19.0-42-generic vmlinux
# ls
vmlinux  vmlinux-5.19.0-41-generic  vmlinux-5.19.0-42-generic
```

Download kernel Source

My installation did not have the necessary sources to build script `vmlinux-gdb.py`. So, I first had to download the kernel source from github.

```
# git clone git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
# uname -a
# git tag
...
# git checkout v5.19
```

Install dependencies required by `make`

```
sudo apt install flex
sudo apt install bison
```

Build `vmlinux-gdb.py`

This script is required for debugging in gdb.

```
# cd /usr/src/linux
# ls
...
Makefile
...
# sudo make scripts_gdb
```

Build Linux Modules

I am not sure whether this is required.

```
# sudo apt install libssl-dev
# sudo apt install libelf-dev
/usr/lib/modules/5.19.0-42-generic/build# sudo make modules

```

Run GDB

```
sudo gdb
```

Configure Files in GDB

```
(gdb) cd /usr/lib/modules/5.19.0-42-generic/build
(gdb) python sys.path.append('/usr/src/linux/scripts/gdb')
(gdb) add-auto-load-safe-path /usr/lib/modules/5.19.0-42-generic/build
(gdb) source /usr/src/linux/vmlinux-gdb.py
(gdb) file /usr/lib/debug/boot/vmlinux
Load new symbol table from "/usr/lib/debug/boot/vmlinux"? (y or n) y

```


# Links

* https://wiki.st.com/stm32mpu/wiki/Debugging_the_Linux_kernel_using_the_GDB#Enabling_Linux_awareness
* https://hamisme.blogspot.com/2013/07/install-vmlinux-on-ubunut.html
* https://kernelnewbies.kernelnewbies.narkive.com/j93AGe2V/gdb-for-kernel-debugging
* https://docs.kernel.org/dev-tools/gdb-kernel-debugging.html
* https://www.kernel.org/doc/html/v4.18/dev-tools/kgdb.html
* https://www.hiroom2.com/2016/07/20/ubuntu-16-04-debug-ubuntu-16-04-kernel-with-qemu-gdb-stub/
* https://wiki.st.com/stm32mpu/wiki/GDB_commands
* https://docs.kernel.org/dev-tools/gdb-kernel-debugging.html



