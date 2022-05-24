
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

title db '# Conditional move', 0x0A, 0x00

subtitle1 db '-> cmovz when ZF = 0', 0x00
subtitle2 db '-> cmovnz when ZF = 0', 0x00
subtitle3 db '-> cmovz when ZF = 1', 0x00
subtitle4 db '-> cmovnz when ZF = 1', 0x00

values db 11, 22, 33, 44, 55, 0x00

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

demo_cmov:
    jmp .demo_body
    .demo_body:

    ; zero flag
    mov eax, subtitle1
    call sprintLF

    mov eax, 0
    movzx ecx, byte [values]
    mov edx, 77
    cmp eax, 0
    cmovz edx, ecx
    mov eax, edx
    call iprintLF

    mov eax, subtitle2
    call sprintLF

    mov eax, 0
    movzx ecx, byte [values]
    mov edx, 77
    cmp eax, 0
    cmovnz edx, ecx
    mov eax, edx
    call iprintLF

    mov eax, subtitle3
    call sprintLF

    mov eax, 1
    movzx ecx, byte [values]
    mov edx, 77
    cmp eax, 0
    cmovz edx, ecx
    mov eax, edx
    call iprintLF

    mov eax, subtitle4
    call sprintLF

    mov eax, 1
    movzx ecx, byte [values]
    mov edx, 77
    cmp eax, 0
    cmovnz edx, ecx
    mov eax, edx
    call iprintLF

    ret

_start:
    call printstart

    mov eax, title
    call sprintLF

    call demo_cmov

    call printend
    call quit
