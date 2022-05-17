
%include 'src/functions.asm'

SECTION .data
startmsg db '** Hello values vs addresses! **', 0x00
endmsg db '** END **', 0x00

SECTION .bss
first_dword: resb 4
second_dword: resb 4

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

    ; notice that in EAX we can store either actual values
    ; or addresses refering to some memory area

    ; first byte manipulation
    mov eax, first_dword        ; set address of first_dword in eax
    mov dword [eax], 0x66       ; 00 00 00 66
    shl dword [eax], 8          ; 00 00 66 00
    or dword [eax], 0x65        ; 00 00 66 65

    push dword [first_dword]    ; stack 65 66 00 00

    ; second byte manipulation
    mov eax, second_dword       ; set address of second_dword in eax
    mov dword [eax], 0x64       ; 00 00 00 64
    shl dword [eax], 8          ; 00 00 64 00
    or dword [eax], 0x63        ; 00 00 64 63
    shl dword [eax], 8          ; 00 64 63 00
    or dword [eax], 0x62        ; 00 64 63 62
    shl dword [eax], 8          ; 64 63 62 00
    or dword [eax], 0x61        ; 64 63 62 61

    push dword [second_dword]   ; stack 61 62 63 64 65 66 00 00

    mov eax, esp
    call sprintLF

    call printend
    call quit
