
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
    mov eax, msg1 ; set msg1 address
    call sprint

    ; wait for user to input name
    mov eax, sinput
    mov ebx, 255
    call getinput

    ; print hello *name*
    mov eax, msg2
    call sprint

    mov eax, sinput
    call sprint

    ; newline
    call printLF

    ; exiting normally
    call quit
