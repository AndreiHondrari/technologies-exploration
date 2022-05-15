
%include 'src/functions.asm'

SECTION .data
msg1 db 'Hello Several ASCII!', 0x00

SECTION .bss
diff: resw 2
characters: resb 255

SECTION .text
global _start

_start:
    mov eax, msg1
    call sprintLF

    call printLF

    mov [diff], dword 126
    sub [diff], dword 33

    mov edi, characters
    mov ecx, 0

    .addChar:
        cmp ecx, [diff]
        jge .endAddChar

        mov edx, 33 ; edx = 33
        add edx, ecx ; edx = 33 + ecx (0 ... (126 - 33))
        mov [edi+ecx], edx

        inc ecx

        jmp .addChar

    .endAddChar:

    add ecx, 1
    mov [edi+ecx], byte 0x00

    mov eax, edi
    call sprintLF

    call printLF

    call quit
