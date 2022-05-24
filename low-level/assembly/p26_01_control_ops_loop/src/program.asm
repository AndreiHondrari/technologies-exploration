
%include 'src/asmlib/binary.asm'
%include 'src/asmlib/io.asm'
%include 'src/asmlib/numbers.asm'
%include 'src/asmlib/process.asm'
%include 'src/asmlib/string.asm'
%include 'src/asmlib/memory.asm'
%include 'src/asmlib/array.asm'

SECTION .data
start_message db '** Hello control operations! **', 0x00
end_message db '** END **', 0x00

title db '# Loop', 0x0A, 0x00

values db 11, 22, 33, 44, 55, 0x00

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

demo_loop:
    jmp .demo_body
    .demo_body:

    ; std
    mov ecx, 13
    .loop1:
        mov eax, ecx
        call iprintLF
        loop .loop1

    ret

_start:
    call printstart

    mov eax, title
    call sprintLF

    call demo_loop

    call printend
    call quit
