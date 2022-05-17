
%include 'src/functions.asm'

SECTION .data
startmsg db '** Hello math operations! **', 0x00
endmsg db '** END **', 0x00

msg_addition db 'Addition 11 + 22 = ', 0x00
msg_substraction db 'Substraction 367 - 245 = ', 0x00
msg_multiplication db 'Multiplication 11 * 5 = ', 0x00
msg_division db 'Division ', 0x00
msg_division_remainder db ' remainder ', 0x00

SECTION .bss

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

    ; ; Addition
    mov eax, msg_addition
    call sprint

    mov eax, 11
    mov ebx, 22
    add eax, ebx
    call iprintLF

    ; Substraction
    mov eax, msg_substraction
    call sprint

    mov eax, 367
    mov ebx, 245
    sub eax, ebx
    call iprintLF

    ; Multiplication
    mov eax, msg_multiplication
    call sprint

    mov eax, 11
    mov ebx, 15
    mul ebx
    call iprintLF

    ; Division
    mov eax, msg_division
    call sprint

    mov edx, 0
    mov eax, 28
    mov ebx, 7
    div ebx

    push edx ; stack the remainder
    push eax ; stack the quotient
    pop eax ; pop the quotient
    call iprint ; print quotient

    mov eax, msg_division_remainder
    call sprint

    pop eax ; pop the remainder
    call iprintLF ; print remainder

    call printend
    call quit
