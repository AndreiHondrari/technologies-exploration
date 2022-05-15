; adding a 0x00 to the end of the strings will prevent from SIGSEGV

%include 'src/functions.asm'

section .data
    ; terminating strings with nullbyte 0x00
    msg1 db 'Hello includes!', 0x0A, 0x00 ; 0x0A = 10 is ASCII code for newline
    msg2 db 'Potatoes are life and blood ...', 0x0A, 0x00

section .text
    global _start

_start:
    mov eax, msg1 ; set string address arg
    call sprint

    mov eax, msg2 ; set string address arg
    call sprint

    ; exiting normally
    call quit
