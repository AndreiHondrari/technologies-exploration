nasm -fbin src/bootloader.asm -o dist/bootloader.bin
nasm -fbin src/kernel.asm -o dist/kernel.bin
cat dist/bootloader.bin dist/kernel.bin > dist/real_os.bin
