
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

title db '# XCHG - Exchange', 0x0A, 0x00

original_ebx db 'Original EBX: ', 0x00
changed_ebx db 'Post EBX: ', 0x00
original_ecx db 'Original ECX: ', 0x00
changed_ecx db 'Post ECX: ', 0x00

exchange_message db 'Exchange EBX and ECX ...', 0x00

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

demo_exchange:
    ; XCHG

    mov ebx, 11
    mov ecx, 22

    mov eax, original_ebx
    call sprint
    mov eax, ebx
    call iprintLF

    mov eax, original_ecx
    call sprint
    mov eax, ecx
    call iprintLF

    mov eax, exchange_message
    call sprintLF
    xchg ebx, ecx

    mov eax, changed_ebx
    call sprint
    mov eax, ebx
    call iprintLF

    mov eax, changed_ecx
    call sprint
    mov eax, ecx
    call iprintLF
    ret

_start:
    call printstart

    mov eax, title
    call sprintLF

    call demo_exchange

    call printend
    call quit
