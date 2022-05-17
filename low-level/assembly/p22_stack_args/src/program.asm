
%include 'src/asmlib/binary.asm'
%include 'src/asmlib/io.asm'
%include 'src/asmlib/numbers.asm'
%include 'src/asmlib/process.asm'
%include 'src/asmlib/string.asm'

STACK_BITS_OFFSET equ 4

SECTION .data
startmsg db '** Hello stack args! **', 0x00
endmsg db '** END **', 0x00

printno db 'Print #', 0x00

SECTION .bss
pintegers_iarray_count: resd 1

SECTION .text
global _start

printstart:
    mov eax, startmsg
    call sprintLF
    call printLF
    ret

printend:
    call printLF
    mov eax, endmsg
    call sprintLF
    ret

_start:
    call printstart

    push 11
    push 22
    push 33
    mov ecx, 3

    mov eax, printno
    call sprint
    mov eax, 1
    call iprintLF
    call print_stack_integers ; our subroutine that uses the stack
    call printLF

    mov eax, printno
    call sprint
    mov eax, 2
    call iprintLF
    call print_stack_integers ; our subroutine that uses the stack
    call printLF

    mov eax, printno
    call sprint
    mov eax, 3
    call iprintLF
    call print_stack_integers ; our subroutine that uses the stack

    call printend
    call quit
