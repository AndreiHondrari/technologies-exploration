
%include 'src/functions.asm'

SECTION .data
startmsg db '** Hello bappend! **', 0x00
endmsg db '** END **', 0x00

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

    mov ebx, char_array ; store char_array into ebx
    mov edi, 0 ; initialize char_array cursor with 0

    ; 4 bytes
    mov eax, 'a'
    call  bappend
    mov eax, 'b'
    call  bappend
    mov eax, 'c'
    call  bappend
    mov eax, 'd'
    call  bappend

    ; another 4 bytes
    mov eax, 'e'
    call  bappend
    mov eax, 'f'
    call  bappend
    mov eax, 'g'
    call  bappend
    mov eax, 'h'
    call  bappend

    ; safety EOL
    mov eax, 0x00
    call  bappend

    mov eax, char_array
    call sprintLF

    call printend
    call quit
