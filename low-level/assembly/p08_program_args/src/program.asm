
%include 'src/functions.asm'

section .data
    ; 0x00 is string termination nullbyte
    msg db 'Hello program args!', 0x00

section .text
    global _start

_start:
    pop ecx ; get number of arguments

    mov eax, msg ; set msg string address
    call sprintLF

    .nextarg:
        cmp ecx, 0
        je .nomoreargs

        pop eax ; set param string address
        call sprintLF

        dec ecx
        jmp .nextarg

    .nomoreargs:

    ; exiting normally
    call quit
