
%include 'src/asmlib/binary.asm'
%include 'src/asmlib/io.asm'
%include 'src/asmlib/numbers.asm'
%include 'src/asmlib/process.asm'
%include 'src/asmlib/string.asm'
%include 'src/asmlib/memory.asm'
%include 'src/asmlib/array.asm'

SECTION .data
start_message db '** Hello transfer operations! **', 0x00
end_message db '** END **', 0x00

title db '# Load effective address', 0x0A, 0x00



; 0x0A = 11
; 0x16 = 22
; 0x21 = 33
; 0x2C = 44
; 0x37 = 55
values db 0x0A, 0x16, 0x21, 0x2C, 0x37, 0x00

SECTION .bss
val1 resb 1
val2 resb 1
val3 resb 1

SECTION .text
global _start

printstart:
    mov eax, start_message
    call sprintLF
    call printLF
    ret

printend:
    call printLF
    mov eax, end_message
    call sprintLF
    ret

demo_lea:
    jmp .demo_body
    .demo_body:

    ; EAX will receive offseted addresses
    ; The idea of LEA is that instead of copying the value from
    ; a square bracket expression, it actually copies the address.
    ; helps if you want to do inline address offseting without
    ; having to do multiple movs and adds

    lea eax, [values+1] ; offset address by 1 byte
    mov edx, [eax]
    mov [val1], edx

    lea eax, [values+2] ; offset address by 2 bytes
    mov edx, [eax]
    mov [val2], edx

    lea eax, [values+3] ; offset address by 3 bytes
    mov edx, [eax]
    mov [val3], edx

    movzx eax, byte [val1] ; move 1 byte from val1
    call iprintLF

    movzx eax, byte [val2] ; move 1 byte from val2
    call iprintLF

    movzx eax, byte [val3] ; move 1 byte from val3
    call iprintLF

    ret

_start:
    call printstart

    mov eax, title
    call sprintLF

    call demo_lea

    call printend
    call quit
