
section .data
    msg db 'Czesc mundo!', 0Ah ; 0x0A = 10 is ASCII code for newline

section .text
    global _start


_start:
    ; write something to console
    mov edx, 13 ; load the length of the string (Czesc mundo! + the 0Ah)
    mov ecx, msg ; load address of our string
    mov ebx, 1 ; the output file descriptor (STDOUT = 1)
    mov eax, 4 ; linux opcode for sys_write
    int 80h ; call linux interrupt

    ; exiting normally
    mov ebx, 0 ; set exit code
    mov eax, 1 ; set opcode for sys_exit
    int 80h ; call linux interrupt
