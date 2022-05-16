
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

    ; in the stack in the end we will have
    ; 61 62 63 64
    ; 65 66 00 00

    ; first dword
    mov eax, 0x66   ; 0x 00 00 00 65
    shl eax, 8      ; 0x 00 00 65 00
    mov al, 0x65    ; 0x 00 00 65 66

    push eax

    ; second dword
    mov eax, 0x64   ; 0x 00 00 00 61
    shl eax, 8      ; 0x 00 00 61 00
    mov al, 0x63    ; 0x 00 00 61 62
    shl eax, 8      ; 0x 00 61 62 00
    mov al, 0x62    ; 0x 00 61 62 63
    shl eax, 8      ; 0x 61 62 63 00
    mov al, 0x61    ; 0x 61 62 63 64

    push eax

    mov eax, esp
    call sprintLF

    pop eax
    pop eax

    call printend
    call quit
