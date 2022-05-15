
%include 'src/functions.asm'

section .data
    ; 0x00 is string termination nullbyte
    msg1 db 'Hello linefeeds and ESP!', 0x00
    msg2 db '% The hunter is out but foxes are partying %', 0x00

section .text
    global _start

_start:
    mov ebx, msg1 ; load the message address arg for the strlen subroutine
    call sprintLF
    
    mov ebx, msg2 ; load the message address arg for the strlen subroutine
    call sprintLF

    ; exiting normally
    call quit
