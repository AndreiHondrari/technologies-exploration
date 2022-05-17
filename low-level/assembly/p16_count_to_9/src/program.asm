
%include 'src/functions.asm'

SECTION .data
startmsg db '** Hello 9 count! **', 0x00
endmsg db '** END **', 0x00

SECTION .bss
char_array: resb 255

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

    mov edi, 0  ; set our char_array cursor to 0

    ; loop from numbers 0 to 9
    mov ebx, 0
    .loop1:
        cmp ebx, 9
        jg .endLoop1

        mov edx, ebx    ; save our current number in edx

        ; 0x30 = decimal 48 = '0'
        ; 0x31 = decimal 49 = '1'
        ; etc.
        add edx, 0x30   ; calculate the ASCII value of our number

        ; append the ASCII value of our number to the array
        push ebx        ; store the current number on stack

        mov eax, edx            ; set eax to our ASCII value
        mov ebx, char_array     ; set ebx to our char array
        call bappend            ; append the ASCII value

        pop ebx         ; restore our current number from the stack

        inc ebx
        jmp .loop1

    .endLoop1:

    mov eax, char_array
    call sprintLF

    call printend
    call quit
