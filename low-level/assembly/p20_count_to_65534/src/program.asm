
%include 'src/functions.asm'

SECTION .data
startmsg db '** Hello Char! **', 0x00
endmsg db '** END **', 0x00

SECTION .bss
number: resd 1

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

    mov ecx, 0
    .loop1:
        cmp ecx, 0x0000FFFF
        je .endLoop1

        ; generate array of digits from a given integer
        mov dword [number], ecx

        push ecx ; stash loop counter

        mov dword eax, [number]
        call iprintLF

        pop ecx ; restore loop counter

        inc ecx
        jmp .loop1

    .endLoop1:

    call printend
    call quit
