
%include 'src/functions.asm'

section .data
    msg db 'Hello includes!', 0Ah ; 0x0A = 10 is ASCII code for newline

section .text
    global _start

_start:
    mov ebx, msg ; load the message address arg for the strlen subroutine
    call strlen

    mov ecx, msg ; load the message address arg for the puts subroutine
    call puts

    ; exiting normally
    call quit
