
%include 'src/functions.asm'

SECTION .data
msg1 db 'Hello ASCII!', 0x00

SECTION .bss
characters: resb 255

SECTION .text
global _start

_start:
    mov eax, msg1
    call sprintLF

    mov edi, characters
    mov [edi], byte 'a'
    mov [edi+1], byte 'b'
    mov [edi+2], byte 'c'
    mov [edi+3], byte 'd'
    mov [edi+4], byte 'e'
    mov [edi+5], byte 0x00

    mov eax, edi
    call sprintLF

    call printLF

    call quit
