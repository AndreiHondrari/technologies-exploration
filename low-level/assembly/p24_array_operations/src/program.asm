
%include 'src/asmlib/binary.asm'
%include 'src/asmlib/io.asm'
%include 'src/asmlib/numbers.asm'
%include 'src/asmlib/process.asm'
%include 'src/asmlib/string.asm'
%include 'src/asmlib/memory.asm'
%include 'src/asmlib/array.asm'

SECTION .data
startmsg db '** Hello arrays! **', 0x00
endmsg db '** END **', 0x00

msg1 db '# Append some value in the array', 0x0A, 0x00
msg2 db '# Display the values from the array', 0x0A, 0x00
msg3 db 'Adding: ', 0x00

ARRAY_SIZE dd 5 ; 5 items in the array
ARRAY_VALUE_SIZE dd 4 ; make the array items integer (4 bytes)

SECTION .bss
array_address: resd 1
value: resd 1

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

    ; allocate an array
    mov eax, [ARRAY_SIZE]
    mov ebx, [ARRAY_VALUE_SIZE]
    mul ebx ; eax = ARRAY_SIZE * ARRAY_VALUE_SIZE (our array in full bytes size)
    call malloc
    mov [array_address], eax ; save our array address

    ; set some values in the array
    mov eax, msg1
    call sprintLF

    mov ecx, 0
    .loop1:
        cmp ecx, [ARRAY_SIZE]
        jg .endLoop1

        ; just print something nice
        mov eax, msg3
        call sprint

        ; create our value (11 .. 55)
        mov eax, ecx
        add eax, 1 ; 0->1, 1->2, ..., 4->5
        mov ebx, 11 ; 11, 22, 33, 44, 55
        mul ebx
        call iprintLF

        mov [value], eax

        mov eax, [array_address]
        mov ebx, value
        ; ecx will be 0 -> 4 (5 items)
        mov edx, 4 ; 4 bytes per item (integer size)
        call array_set

        inc ecx
        jmp .loop1
    .endLoop1:


    ; print the array values
    call printLF
    mov eax, msg2
    call sprintLF

    mov ecx, 0
    .loop2:
        cmp ecx, [ARRAY_SIZE]
        jg .endLoop2

        mov eax, [array_address]
        mov ebx, value
        ; ecx will be 0 -> 4 (5 items)
        mov edx, 4 ; 4 bytes per item (integer size)
        call array_get

        mov eax, [value]
        call iprintLF

        inc ecx
        jmp .loop2

    .endLoop2:

    call printend
    call quit
