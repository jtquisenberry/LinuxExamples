# hexdump

# Examples


## Offsets

* `-n` specifies the length in bytes.
* `-s` specifies the offset (where to start reading).

`-s` MUST be specified in hexadecimal format.

```
hexdump -n 4 -s 0x11C -e '4/1 "%x " "\n"' myFile
```
https://stackoverflow.com/questions/19215180/bash-get-the-bytes-at-offset-for-length


## Read a portion of /dev/mem

Most of /dev/mem is protected, unless certain options are set when compiling the kernel. However, this is how to *try* to read /dev/mem.

```
# hexdump -C /dev/mem | head -5
00000000  53 ff 00 f0 53 ff 00 f0  c3 e2 00 f0 53 ff 00 f0  |S...S.......S...|
00000010  53 ff 00 f0 54 ff 00 f0  88 84 00 f0 53 ff 00 f0  |S...T.......S...|
00000020  a5 fe 00 f0 87 e9 00 f0  56 0d 00 f0 56 0d 00 f0  |........V...V...|
00000030  56 0d 00 f0 56 0d 00 f0  57 ef 00 f0 00 f5 00 f0  |V...V...W.......|
00000040  16 0b 00 c0 4d f8 00 f0  41 f8 00 f0 17 01 00 c8  |....M...A.......|
```

## grep

```
# cd /proc/3526/map_files
# hexdump -C 5627bf812000-5627bf813000 | grep 78
00000240  64 2d 6c 69 6e 75 78 2d  78 38 36 2d 36 34 2e 73  |d-linux-x86-64.s|
000003b0  5f 63 78 61 5f 66 69 6e  61 6c 69 7a 65 00 5f 5f  |_cxa_finalize.__|
00000720  08 20 00 3d 78 56 34 12  74 e9 8b 05 e0 08 20 00  |. .=xV4.t..... .|
00000780  ff 48 85 ed 74 20 31 db  0f 1f 84 00 00 00 00 00  |.H..t 1.........|
000007e0  64 20 25 6a 75 0a 00 69  20 25 6a 78 0a 00 00 00  |d %ju..i %jx....|
00000830  14 00 00 00 00 00 00 00  01 7a 52 00 01 78 10 01  |.........zR..x..|
00000860  14 00 00 00 00 00 00 00  01 7a 52 00 01 78 10 01  |.........zR..x..|
00001010  78 56 34 12 47 43 43 3a  20 28 55 62 75 6e 74 75  |xV4.GCC: (Ubuntu|
000016a0  72 73 5f 61 75 78 00 63  6f 6d 70 6c 65 74 65 64  |rs_aux.completed|
000016c0  6c 5f 64 74 6f 72 73 5f  61 75 78 5f 66 69 6e 69  |l_dtors_aux_fini|
00001780  63 5f 63 73 75 5f 66 69  6e 69 00 5f 49 54 4d 5f  |c_csu_fini._ITM_|
00001880  5f 32 2e 32 2e 35 00 5f  5f 63 78 61 5f 66 69 6e  |_2.2.5.__cxa_fin|
00001940  2e 74 65 78 74 00 2e 66  69 6e 69 00 2e 72 6f 64  |.text..fini..rod|
```


# Links

https://www.baeldung.com/linux/create-hex-dump
