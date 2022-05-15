echo "*** COMPILE ASM PROGRAMS ***"
echo "Generating obj files ..."
nasm -g -F dwarf -f elf src/p01_without_nullbytes.asm -o dist/p01.o
nasm -g -F dwarf -f elf src/p02_with_nullbytes.asm -o dist/p02.o

echo "Linking into executables ..."
ld -m elf_i386 dist/p01.o -o dist/p01
ld -m elf_i386 dist/p02.o -o dist/p02

echo "DONE"
echo ""
