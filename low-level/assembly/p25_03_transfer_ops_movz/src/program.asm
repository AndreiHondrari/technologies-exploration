
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

title db '# Move with Zero Extend', 0x0A, 0x00

msg_ebx db 'EBX: ', 0x00
msg_ecx db 'ECX: ', 0x00

msg_move db 'Move CL to EBX...', 0x00

SECTION .bss

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

demo_movz:

    jmp .demo_body

    .printRegisters:
        mov eax, msg_ebx
        call sprint
        mov eax, ebx
        call iprintLF

        mov eax, msg_ecx
        call sprint
        mov eax, ecx
        call iprintLF

        ret

    .printMove:
        mov eax, msg_move
        call sprintLF
        ret

    .demo_body:

    mov ebx, 0
    mov cl, 22

    call .printRegisters

    movzx ebx, cl
    call .printMove

    call .printRegisters

    ret

_start:
    call printstart

    mov eax, title
    call sprintLF

    call demo_movz

    call printend
    call quit
