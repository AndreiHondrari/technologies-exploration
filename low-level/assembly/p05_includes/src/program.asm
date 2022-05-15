
%include 'src/functions.asm'

section .data
    msg db 'Hello includes!', 0Ah ; 0x0A = 10 is ASCII code for newline

section .text
    global _start

_start:
    mov eax, msg ; set string address arg
    call strlen

    mov ebx, eax ; set string size arg
    mov eax, msg ; set string address arg
    call swrite

    ; exiting normally
    call quit
