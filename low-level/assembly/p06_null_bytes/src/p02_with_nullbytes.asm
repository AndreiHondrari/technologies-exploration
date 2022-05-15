; adding a 0x00 to the end of the strings will prevent from SIGSEGV

%include 'src/functions.asm'

section .data
    ; terminating strings with nullbyte 0x00
    msg1 db 'Hello includes!', 0x0A, 0x00 ; 0x0A = 10 is ASCII code for newline
    msg2 db 'Potatoes are life and blood ...', 0x0A, 0x00

section .text
    global _start

_start:
    mov ebx, msg1 ; load the message address arg for the sprint subroutine
    call sprint

    mov ebx, msg2 ; load the message address arg for the sprint subroutine
    call sprint

    ; exiting normally
    call quit
