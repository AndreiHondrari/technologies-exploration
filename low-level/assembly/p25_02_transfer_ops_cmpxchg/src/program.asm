
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

title db '# CMPXCHG - Conditional Exchange', 0x0A, 0x00

submessage1 db '-> First cmpxchg', 0x0A, 0x00
submessage2 db '-> Second cmpxchg', 0x0A, 0x00
submessage3 db '-> Third cmpxchg', 0x0A, 0x00

original_eax db 'Original EAX: ', 0x00
changed_eax db 'Post EAX: ', 0x00
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

demo_cmp_exchange:
    ; CMPXCHG

    jmp .demo_cmp_exchange_body

    .showPreRegisters:
        push eax

        push eax
        mov eax, original_eax
        call sprint
        pop eax
        call iprintLF

        mov eax, original_ebx
        call sprint
        mov eax, ebx
        call iprintLF

        mov eax, original_ecx
        call sprint
        mov eax, ecx
        call iprintLF

        pop eax
        ret

    .showPostRegisters:
        push eax

        push eax
        mov eax, changed_eax
        call sprint
        pop eax
        call iprintLF

        mov eax, changed_ebx
        call sprint
        mov eax, ebx
        call iprintLF

        mov eax, changed_ecx
        call sprint
        mov eax, ecx
        call iprintLF

        pop eax
        ret

    .printExchange:
        push eax
        mov eax, exchange_message
        call sprintLF
        pop eax
        ret

    .demo_cmp_exchange_body:

    mov eax, 55
    mov ebx, 33
    mov ecx, 44

    ; show before the exchange
    call .showPreRegisters
    call printLF

    ; <------------->
    ; FIRST exchange
    ;
    ; In this sample we have:
    ; EAX = 55
    ; EBX = 33
    ; ECX = 44
    ;
    ; Exchange happens between EBX and ECX.
    ; Since EBX != EAX, EAX is then set with the value from EBX
    ;
    ; EAX = 33
    ; EBX = 33
    ; ECX = 44

    mov eax, submessage1
    call sprintLF

    call .printExchange
    cmpxchg ebx, ecx

    ; show after the exchange
    call .showPostRegisters

    ; <------------->
    ; SECOND exchange
    ;
    ; Since our previous run EAX has been loaded with the value from EBX
    ; hence now we have:
    ; EAX = 33
    ; EBX = 33
    ; ECX = 44
    ;
    ; EAX == EBX so the result is that EBX loads the value from ECX
    ;
    ; EAX = 33
    ; EBX = 44
    ; ECX = 44
    ;
    ; basically it means that calling cmpxchg two times results in this
    ; behaviour.
    ;

    push eax
    call printLF
    mov eax, submessage2
    call sprintLF
    pop eax

    call .printExchange
    cmpxchg ebx, ecx

    ; show after the exchange
    call .showPostRegisters

    ; <------------->
    ; THIRD exchange
    ;
    ; Called a third time with the previous values results in
    ; having all operands propagated with the original value from the
    ; second operand of the cmpxchg, which in our case is ECX.
    ;
    ; EAX = 44
    ; EBX = 44
    ; ECX = 44

    push eax
    call printLF
    mov eax, submessage3
    call sprintLF
    pop eax

    ; mov eax, 33
    ; mov ebx, 33
    ; mov ecx, 44

    call .printExchange
    cmpxchg ebx, ecx

    ; show after the exchange
    call .showPostRegisters

    ret

_start:
    call printstart

    mov eax, title
    call sprintLF

    call demo_cmp_exchange

    call printend
    call quit
