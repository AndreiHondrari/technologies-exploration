
%include 'src/functions.asm'

section .data
    ; 0x00 is string termination nullbyte
    msg1 db 'Hello program args!', 0x00
    msg2 db 'Far over, the misty mountains cold', 0x00

section .text
    global _start

_start:
    pop ecx ; get number of arguments

    mov ebx, msg1
    call sprintLF

    .nextarg:
        cmp ecx, 0
        je .nomoreargs

        pop ebx
        call sprintLF

        dec ecx
        jmp .nextarg

    .nomoreargs:

    ; exiting normally
    call quit
