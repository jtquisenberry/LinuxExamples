#include <linux/module.h>    // included for all kernel modules
#include <linux/kernel.h>    // included for KERN_INFO
#include <linux/init.h>      // included for __init and __exit macros

MODULE_LICENSE("GPL");
MODULE_AUTHOR("TestUser");
MODULE_DESCRIPTION("A Simple Hello World module");

static int __init hello_init(void)
{
    phys_addr_t addr = 0xf53891010;
    //int* addr2 = (int*) 0xf53891010;
    printk(KERN_INFO "addr %pa\n", &addr );
    printk(KERN_INFO "value %llx\n", addr );
    //printk(KERN_INFO "value %x\n", *addr2);
    return 0;    // Non-zero return means that the module couldn't be loaded.
}

static void __exit hello_cleanup(void)
{
    printk(KERN_INFO "Cleaning up module.\n");
}

module_init(hello_init);
module_exit(hello_cleanup);
