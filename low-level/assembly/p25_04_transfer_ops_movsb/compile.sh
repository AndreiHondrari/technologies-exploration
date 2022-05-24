echo "*** COMPILE ASM PROGRAM ***"
echo "Generating obj file ..."
nasm -g -F dwarf -f elf src/program.asm -o dist/program.o

echo "Linking into executable ..."
ld -m elf_i386 dist/program.o -o dist/program

echo "DONE"
echo ""
