# Paths

```
$ sudo cat /proc/kallsyms
...
ffffffff97d7aed0 t liquidio_pcie_mmio_enabled   [liquidio]
ffffffff97d7aef0 t liquidio_pcie_resume [liquidio]
ffffffff97d7af00 t liquidio_ptp_adjtime [liquidio]
ffffffff97d7af50 t liquidio_ptp_enable  [liquidio]
```

List all symbols that the kernel is aware of. The second column has these meanings:
* "T": text area and exported.
* "t": text area NOT exported.
* "D": data area and exported.
* "d": data area NOT exported. 
