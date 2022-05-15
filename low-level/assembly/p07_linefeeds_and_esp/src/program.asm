; Notice in this example we don't use 0x0A
; directly in the string data anymore

%include 'src/functions.asm'

section .data
    ; 0x00 is string termination nullbyte
    msg1 db 'Hello linefeeds and ESP!', 0x00
    msg2 db '% The hunter is out but foxes are partying %', 0x00

section .text
    global _start

_start:
    mov eax, msg1 ; set the first msg address
    call sprintLF
    call sprintLF

    mov eax, msg2 ; set the second msg address
    call sprintLF
    call sprintLF

    ; exiting normally
    call quit
