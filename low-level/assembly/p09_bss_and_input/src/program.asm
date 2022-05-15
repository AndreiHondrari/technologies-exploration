
%include 'src/functions.asm'

section .data
    ; 0x00 is string termination nullbyte
    msg1 db 'Enter your name: ', 0x00
    msg2 db 'Greetings ', 0x00

section .bss
sinput: RESB 255

section .text
    global _start

_start:
    ; ask for name
    mov ebx, msg1
    call sprint


    ; wait for user to input name
    mov eax, sinput
    mov edx, 255
    call getinput

    ; print hello *name*
    mov ebx, msg2
    call sprint
    mov ebx, sinput
    call sprint

    ; newline
    call printLF

    ; exiting normally
    call quit
