
%include 'src/functions.asm'

SECTION .data
startmsg db '** Hello Char! **', 0x00
endmsg db '** END **', 0x00

SECTION .bss
number: resd 1
digits: resb 255
digits_count: resd 1
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

    ; generate array of digits from a given integer
    mov dword [number], 11223344
    mov dword eax, [number]
    mov edi, digits
    call itoa
    mov dword [digits_count], ecx

    ; convert all digits to ASCII codes
    mov esi, digits
    mov edi, char_array
    call convert_digits_to_ascii

    inc ecx
    mov byte [char_array+ecx], 0x00

    ; print digits
    mov eax, char_array
    call sprintLF

    call printend
    call quit
