
%include 'src/functions.asm'

SECTION .data
startmsg db '** Hello Char! **', 0x00
endmsg db '** END **', 0x00
some_message db "You can not move forward in an absence of space.", 0x00

SECTION .bss
char_array: resb 255

SECTION .text
global _start

printstart:
    mov eax, startmsg
    call sprintLF
    call printLF
    ret

printend:
    call printLF
    mov eax, endmsg
    call sprintLF
    ret

_start:
    call printstart

    ; count characters in our source message
    mov eax, some_message
    call strlen

    ; copy characters from source to destination
    mov esi, some_message
    mov edi, char_array
    mov ebx, eax
    call bcopy

    mov eax, char_array
    call sprintLF

    call printend
    call quit
