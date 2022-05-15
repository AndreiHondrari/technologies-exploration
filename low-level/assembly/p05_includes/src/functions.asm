
strlen: ; define the strlen subroutine
    mov edx, 0 ; edx counts the number of characters

    .nextchar:
    cmp byte [ebx], 0 ; check if end of string (nullbyte)
    je .endcount
    inc edx
    inc ebx
    jmp .nextchar
    .endcount:
    ret

puts:
    mov eax, 4
    mov ebx, 1
    int 80h
    ret

quit:
    mov ebx, 0 ; set exit code
    mov eax, 1 ; set opcode for sys_exit
    int 80h ; call linux interrupt
    ret
