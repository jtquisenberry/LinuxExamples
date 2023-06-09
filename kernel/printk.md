#printk



# Format Specifiers

Integer Types

```
If variable is of Type,         use printk format specifier:
------------------------------------------------------------
        char                    %d or %x
        unsigned char           %u or %x
        short int               %d or %x
        unsigned short int      %u or %x
        int                     %d or %x
        unsigned int            %u or %x
        long                    %ld or %lx
        unsigned long           %lu or %lx
        long long               %lld or %llx
        unsigned long long      %llu or %llx
        size_t                  %zu or %zx
        ssize_t                 %zd or %zx
        s8                      %d or %x
        u8                      %u or %x
        s16                     %d or %x
        u16                     %u or %x
        s32                     %d or %x
        u32                     %u or %x
        s64                     %lld or %llx
        u64                     %llu or %llx
```

# Physical Addresses

```
phys_addr_t paddr = 0x1234;
printk(KERN_INFO "%pa\n", &paddr);
// Result: 0x0000000000001234
```
https://stackoverflow.com/questions/73774516/how-to-use-printk-to-print-a-physical-address-aka-phys-addr-t


# Links

https://docs.kernel.org/core-api/printk-formats.html

https://stackoverflow.com/questions/73774516/how-to-use-printk-to-print-a-physical-address-aka-phys-addr-t
