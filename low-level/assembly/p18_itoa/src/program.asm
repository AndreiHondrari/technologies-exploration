
%include 'src/functions.asm'

SECTION .data
startmsg db '** Hello integer-to-array! **', 0x00
endmsg db '** END **', 0x00

SECTION .bss

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

    mov eax, 11223344
    call iprintLF

    call printend
    call quit
