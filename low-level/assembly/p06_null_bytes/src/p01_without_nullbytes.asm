
%include 'src/functions.asm'

section .data
    msg1 db 'Hello includes!', 0Ah ; 0x0A = 10 is ASCII code for newline
    msg2 db 'Potatoes are life and blood ...', 0Ah

section .text
    global _start

_start:
    mov ebx, msg1 ; load the message address arg for the sprint subroutine
    call sprint

    ; mov ebx, msg2 ; load the message address arg for the sprint subroutine
    call sprint

    ; exiting normally
    call quit
