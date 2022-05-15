
section .data
    msg db 'Czesc mundo!', 0Ah ; 0x0A = 10 is ASCII code for newline

section .text
    global _start


_start:
    mov edx, 13 ; load the length of the string
    mov ecx, msg ; load address of our string
    mov ebx, 1 ; the output file descriptor (STDOUT = 1)
    mov eax, 4 ; linux opcode for sys_write
    int 80h

    ; it is normal that it will throw a SIGSEGV
    ; because we are not existing normally
    ; meaning in Linux we are not
    ; caling sys_exit at the end
