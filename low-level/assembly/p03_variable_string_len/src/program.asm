
section .data
    msg db 'Hello in a world with infinite possibilities!', 0Ah ; 0x0A = 10 is ASCII code for newline

section .text
    global _start



_start:

    mov ebx, msg

    mov edx, 0

    countchar:
        cmp byte [ebx], 0 ; check if end of string (nullbyte)
        je endcountchar
        inc edx
        inc ebx
        jmp countchar

    endcountchar:

    mov eax, 4
    mov ebx, 1
    mov ecx, msg
    int 80h

    ; exiting normally
    mov ebx, 0 ; set exit code
    mov eax, 1 ; set opcode for sys_exit
    int 80h ; call linux interrupt
