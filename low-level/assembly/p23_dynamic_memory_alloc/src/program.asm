
%include 'src/asmlib/binary.asm'
%include 'src/asmlib/io.asm'
%include 'src/asmlib/numbers.asm'
%include 'src/asmlib/process.asm'
%include 'src/asmlib/string.asm'
%include 'src/asmlib/memory.asm'

SECTION .data
startmsg db '** Hello dynamic memory allocation! **', 0x00
endmsg db '** END **', 0x00

msg1 db '# Integer allocation', 0x0A, 0x00
msg2 db '# With malloc', 0x0A, 0x00
msg3 db '# String allocation', 0x0A, 0x00

sometext db 'Dabadee dabadoo. Yabadabadoo', 0x00

SECTION .bss
string_address: resd 1

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

    ; according to
    ;   - https://github.com/torvalds/linux/blob/master/include/uapi/asm-generic/mman-common.h
    ;   - https://github.com/torvalds/linux/blob/master/include/uapi/linux/mman.h
    ;
    ; PROT_READ =       0x01
    ; PROT_WRITE =      0x02
    ; PROT_EXEC =       0x03
    ;
    ; MAP_PRIVATE =     0x02
    ; MAP_ANONYMOUS =   0x20

    ; allocate for integer
    mov eax, msg1
    call sprintLF

    ; eax will become the new allocated memory address after the execution
    mov eax, 192    ; sys_mmap2 opcode (0xC0)
    mov ebx, 0      ; address = NULL
    mov ecx, 4      ; length
    mov edx, 1      ; proto = 1 (read)
    or edx, 2       ; proto = 1 | 2 (read and write)
    mov esi, 0x02   ; flags = 2 (map_private)
    or esi, 0x20    ; flags = 2 | 32 (map_private | map_anonymous)
    mov edi, -1     ; file descriptor (requiredd by map_anonymous)
    mov ebp, 0      ; offset = 0
    int 0x80        ; syscall

    mov dword [eax], 1234 ; store a number into the new integer
    mov dword eax, [eax]
    call iprintLF

    ; allocate with malloc
    call printLF
    mov eax, msg2
    call sprintLF

    mov eax, 4 ; 4 bytes = integer
    call malloc

    mov dword [eax], 5678 ; store a number into the new integer
    mov dword eax, [eax]
    call iprintLF

    ; alocate for string
    call printLF
    mov eax, msg3
    call sprintLF

    mov eax, 100
    call malloc
    mov [string_address], eax ; save our new string address

    ; determine the string length
    mov eax, sometext
    call strlen

    ; copy text into the string variable
    mov ebx, eax ; specify the string length to be copied
    mov esi, sometext ; source address (some constant)
    mov edi, string_address ; destination address (our new string)
    call bcopy ; copy the string

    mov eax, string_address
    call sprintLF

    call printend
    call quit
