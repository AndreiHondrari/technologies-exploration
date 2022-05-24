
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

title db '# Move string / bytes', 0x0A, 0x00

msg_output db 'Final output: ', 0x00
msg_char db 'Character: ', 0x00

something db 'ABCDEFGHIJKLMNOPQRSTUVXYZ', 0x00

msg_esi db 'ESI: ', 0x00
msg_edi db 'EDI: ', 0x00
msg_ecx db 'ECX: ', 0x00

msg_registers_before db '-> Registers before', 0x0A, 0x00
msg_registers_after db 0x0A, '-> Registers after', 0x0A, 0x00

msg_move db 0x0A, '--> Move 3 times ...', 0x00
msg_move_repeated db 0x0A, '--> Move repeated ...', 0x00

subtitle1 db '## Manual movsb', 0x0A, 0x00
subtitle2 db '## Repeated movsb', 0x0A, 0x00

SECTION .bss
this: resb 30
that: resb 30

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

demo_movsb:

    jmp .demo_body

    .printRegistersBefore:
        push eax
        mov eax, msg_registers_before
        call sprintLF
        pop eax
        ret

    .printRegistersAfter:
        push eax
        mov eax, msg_registers_after
        call sprintLF
        pop eax
        ret

    .printRegisters:
        mov eax, msg_esi
        call sprint
        mov eax, esi
        call iprintLF

        mov eax, msg_edi
        call sprint
        mov eax, edi
        call iprintLF

        ret

    .printECX:
        mov eax, msg_ecx
        call sprint
        mov eax, ecx
        call iprintLF
        ret

    .printMove:
        mov eax, msg_move
        call sprintLF
        ret

    .printMoveRepeated:
        mov eax, msg_move_repeated
        call sprintLF
        ret

    .printCharacter:
        pusha

        mov eax, msg_char
        call sprint

        mov eax, [esi]
        ; movzx byte eax, al
        call iprintLF
        popa
        ret

    .demo_manual_movsb:
        ; set the source and destination buffers
        mov esi, something
        mov edi, this

        call .printRegistersBefore
        call .printRegisters
        call .printMove

        ; <---------->
        ; MOVE THREE TIMES
        call demo_movsb.printCharacter
        movsb
        call demo_movsb.printCharacter
        movsb
        nop
        call demo_movsb.printCharacter
        nop
        movsb
        ; MOVING ENDED

        call .printRegistersAfter
        call .printRegisters

        ; put a 0x00 at the end, just to be sure
        mov byte [edi], 0x00

        call printLF
        mov eax, msg_output
        call sprintLF

        mov eax, this
        call sprintLF

        ret

    .demo_repeated_movsb:
        ; set the source and destination buffers
        mov esi, something
        mov edi, that
        mov ecx, 5 ; how many characters we want to copy

        call demo_movsb.printRegistersBefore
        call demo_movsb.printRegisters
        call demo_movsb.printECX
        call demo_movsb.printMoveRepeated

        ; <---------->
        ; MOVE REPEATED
        rep movsb
        ; MOVING ENDED

        call demo_movsb.printRegistersAfter
        call demo_movsb.printRegisters
        call demo_movsb.printECX

        ; put a 0x00 at the end, just to be sure
        mov byte [edi], 0x00

        call printLF
        mov eax, msg_output
        call sprintLF

        mov eax, that
        call sprintLF

        ret

    .demo_body:
        mov eax, subtitle1
        call sprintLF
        call .demo_manual_movsb

        call printLF
        mov eax, subtitle2
        call sprintLF
        call .demo_repeated_movsb
    ret

_start:
    call printstart

    mov eax, title
    call sprintLF

    call demo_movsb

    call printend
    call quit
