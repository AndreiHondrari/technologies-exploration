
section .data
    msg db 'Hello subroutines!', 0Ah ; 0x0A = 10 is ASCII code for newline

section .text
    global _start


; -------------------------------------
; strlen(
;   eax : string address
; ) -> eax : string size
; Calculates the size of the string
strlen: ; define the strlen subroutine
    push ebx

    mov ebx, eax

    .nextchar:
    cmp byte [eax], 0 ; check if end of string (nullbyte)
    jz .endcount
    inc eax
    jmp .nextchar
    .endcount:

    sub eax, ebx ; eax = eax - ebx

    pop ebx
    ret

; -------------------------------------
; swrite(
;   eax : string address,
;   ebx : string size
; )
swrite:
    push eax
    push ebx

    ; load args
    mov ecx, eax ; set string address
    mov edx, ebx ; set string size

    mov eax, 4 ; set sys_write opcode
    mov ebx, 1 ; set filedescriptor to STDOUT=1
    int 80h ; call linux interrupt

    pop ebx
    pop eax
    ret

; -------------------------------------
; quits program
quit:
    mov ebx, 0 ; set exit code
    mov eax, 1 ; set opcode for sys_exit
    int 80h ; call linux interrupt
    ret

_start:
    mov eax, msg ; set string address arg
    call strlen

    mov ebx, eax ; set string length arg
    mov eax, msg ; set string address arg

    ; print three times
    call swrite
    call swrite
    call swrite

    ; exiting normally
    call quit
