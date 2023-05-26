#include <linux/module.h>    // included for all kernel modules
#include <linux/kernel.h>    // included for KERN_INFO
#include <linux/init.h>      // included for __init and __exit macros
#include <linux/futex.h>
#include <kernel/futex.c>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Jacob Quisenberry");
MODULE_DESCRIPTION("Futex Examiner");

static int __init hello_init(void)
{
    union futex_key key1 = FUTEX_KEY_INIT;
    printk(KERN_INFO "Get futex key\n");
    //futex_key key1 = FUTEX_KEY_INIT;
    get_futex_key(0x20566a0, 0, &key1, VERIFY_READ);
    printk(KERN_INFO "key1 = %p\n", &key1);
    return 0;    // Non-zero return means that the module couldn't be loaded.
}

static void __exit hello_cleanup(void)
{
    printk(KERN_INFO "Cleaning up module.\n");
}

module_init(hello_init);
module_exit(hello_cleanup);
