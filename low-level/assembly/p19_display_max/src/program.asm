
%include 'src/functions.asm'

SECTION .data
startmsg db '** Hello Char! **', 0x00
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

    ; generate array of digits from a given integer
    mov eax, 0xFFFFFFFF ; 4 294 967 295 (10 bytes)
    call iprintLF

    call printend
    call quit
