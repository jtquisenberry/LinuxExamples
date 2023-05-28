# System

* Ubuntu 22.04
* Kernel 5.19.0-42-generic vmlinux


# Setting up Linux Kernel awareness in gdb

My kernel is not setup for GDB. Here is what I did to get `lx-symbols` to work in `gdb`. The results of commands like `lx-ps` do not appear to be complete, though.

Reduced functionality may occur because I did not build the kernel. 

kernel.org lists these setup steps:
* Create a virtual Linux machine for QEMU/KVM (see www.linux-kvm.org and www.qemu.org for more details). For cross-development, https://landley.net/aboriginal/bin keeps a pool of machine images and toolchains that can be helpful to start from.
* Build the kernel with CONFIG_GDB_SCRIPTS enabled, but leave CONFIG_DEBUG_INFO_REDUCED off. If your architecture supports CONFIG_FRAME_POINTER, keep it enabled.
* Install that kernel on the guest, turn off KASLR if necessary by adding "nokaslr" to the kernel command line. Alternatively, QEMU allows to boot the kernel directly using -kernel, -append, -initrd command line switches. This is generally only useful if you do not depend on modules. See QEMU documentation for more details on this mode. In this case, you should build the kernel with CONFIG_RANDOMIZE_BASE disabled if the architecture supports KASLR.

```

     

7月 10, 2013
Install vmlinux on Ubunut
Reference: http://superuser.com/questions/62575/where-is-vmlinux-on-my-ubuntu-installation

Why I need install vmlinux ? Because i will use `crash` tool to debug kernel :D   

you can step by step to install vmlinux on below:

1. apt install vmlinux 

echo "deb http://ddebs.ubuntu.com $(lsb_release -cs)-updates main restricted universe multiverse
deb http://ddebs.ubuntu.com $(lsb_release -cs)-security main restricted universe multiverse
deb http://ddebs.ubuntu.com $(lsb_release -cs)-proposed main restricted universe multiverse" | \
sudo tee -a /etc/apt/sources.list.d/ddebs.list

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 428D7C01

sudo apt-get update
sudo apt-get install linux-image-$(uname -r)-dbgsym


```





```


sudo apt-get install linux-image-$(uname -r)-dbgsym



```

```
cd /usr/lib/debug/boot/vmlinux-$(uname -r)


sudo apt install flex
sudo apt install bison
sudo make scripts_gdb

```



Git

```


git clone git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
uname -a
git tag
git checkout v5.19





```








```

sudo apt install linux-source
sudo apt install libssl-dev
sudo apt install libelf-dev


/usr/lib/modules/5.19.0-42-generic/build# sudo make modules


```



Copy `vmlinux-5.19.0-42 vmlinux to `vmlinux`


```
cp vmlinux-5.19.0-42-generic vmlinux

```



```




cd /usr/lib/modules/5.19.0-42-generic/build
python sys.path.append('/usr/src/linux/scripts/gdb')



add-auto-load-safe-path /usr/lib/modules/5.19.0-42-generic/build
source /usr/src/linux/vmlinux-gdb.py

(gdb) file /usr/lib/debug/boot/vmlinux
Load new symbol table from "/usr/lib/debug/boot/vmlinux"? (y or n) y



```


# Links

* https://wiki.st.com/stm32mpu/wiki/Debugging_the_Linux_kernel_using_the_GDB#Enabling_Linux_awareness
* https://hamisme.blogspot.com/2013/07/install-vmlinux-on-ubunut.html
* https://kernelnewbies.kernelnewbies.narkive.com/j93AGe2V/gdb-for-kernel-debugging
* 



