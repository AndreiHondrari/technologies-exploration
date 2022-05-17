
%include 'src/functions.asm'

SECTION .data
startmsg db '** Hello manually placed chars! **', 0x00
endmsg db '** END **', 0x00

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

    ; the idea is that on the stack
    ; sets of 4 bytes (dwords) are being stored
    ; and since 1 characters equals 1 byte,
    ; if our character is ASCII code 97 = 0x61 = 'a'
    ; then in the stack we would have
    ; 0x61 0x00 0x00 0x00 or 0x00000061
    ;
    ; when sprint cruises over the stack starting from 0x61
    ; the second byte it hits is 0x00 which
    ; qualifies for EOL, hence there is no need
    ; to manually specify 0x00 on the stack
    ;
    ; Notice the characters are printed in reverse
    ; because the ESP always points to the last byte introduced
    ; and it works upwards in the reverse order the bytes were stored

    ; store one character
    mov eax, 'a' ; 0x 00 00 00 61
    push eax

    ; print 'a'
    mov eax, esp
    call sprintLF

    pop eax ; restore eax as 'a'

    ; add two more characters to the DWORD
    shl eax, 8      ; 0x 00 00 61 00
    mov al, 0x62    ; 0x 00 00 61 62

    shl eax, 8      ; 0x 00 61 62 00
    mov al, 0x63    ; 0x 00 61 62 63

    push eax

    ; print 'abc'
    mov eax, esp
    call sprintLF

    pop eax ; restore 0x 00 61 62 63

    call printend
    call quit
