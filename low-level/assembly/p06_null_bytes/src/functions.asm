
strlen: ; define the strlen subroutine
    push ebx  ; snapshot for state restoration

    mov edx, 0 ; edx counts the number of characters

    .nextchar:
    cmp byte [ebx], 0 ; check if end of string (nullbyte)
    je .endcount
    inc edx
    inc ebx
    jmp .nextchar
    .endcount:

    pop ebx ; state restoration

    ret

puts:
    pusha ; snapshot for state restoration (all)

    mov eax, 4
    mov ebx, 1
    int 80h

    popa ; state restoration (all)

    ret

sprint:
    push ebx ; snapshot for state restoration

    call strlen
    mov ecx, ebx ; put the string address into ecx
    call puts

    pop ebx ; state restoration

    ret

quit:
    mov ebx, 0 ; set exit code
    mov eax, 1 ; set opcode for sys_exit
    int 80h ; call linux interrupt
    ret
