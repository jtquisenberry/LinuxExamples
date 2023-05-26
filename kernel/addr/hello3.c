#include <linux/module.h>    // included for all kernel modules
#include <linux/kernel.h>    // included for KERN_INFO
#include <linux/init.h>      // included for __init and __exit macros
#include <asm/io.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Lakshmanan");
MODULE_DESCRIPTION("A Simple Hello World module");

static int __init hello_init(void)
{
    phys_addr_t paddr = 0x22f227010;
    void * vaddr = phys_to_virt(paddr);
    //int* addr2 = (int*) 0x22f227010;
    printk(KERN_INFO "Physical Address: &paddr %pa\n", &paddr );
    printk(KERN_INFO "Physical Address: paddr %llx\n", paddr );
    printk(KERN_INFO "Virtual Address in Kernel: vaddr 0x%p\n", vaddr );
    printk(KERN_INFO "Virtual Address Value:  *((int*)vaddr) value 0x%x\n", *((int*)vaddr));
    //printk(KERN_INFO "value %x\n", *addr2);
    return 0;    // Non-zero return means that the module couldn't be loaded.
}

static void __exit hello_cleanup(void)
{
    printk(KERN_INFO "Cleaning up module.\n");
}

module_init(hello_init);
module_exit(hello_cleanup);
