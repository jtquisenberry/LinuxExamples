cmd_/home/useradmin/git/LinuxExamples/kernel/addr2/hello2.ko := ld -r -m elf_x86_64 -z max-page-size=0x200000 -z noexecstack  -T ./scripts/module-common.lds --build-id  -o /home/useradmin/git/LinuxExamples/kernel/addr2/hello2.ko /home/useradmin/git/LinuxExamples/kernel/addr2/hello2.o /home/useradmin/git/LinuxExamples/kernel/addr2/hello2.mod.o ;  true