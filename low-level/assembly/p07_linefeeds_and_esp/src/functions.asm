
; ------------------------------------
; strlen(ebx : address of string) -> eax : length of string
strlen: ; define the strlen subroutine
    ; snapshot for state restoration
    push ebx

    mov eax, 0 ; counts the number of characters

    .nextchar:
    cmp byte [ebx], 0 ; check if end of string (nullbyte)
    je .endcount
    inc eax ; increase count
    inc ebx ; select next character
    jmp .nextchar
    .endcount:

    ; state restoration
    pop ebx

    ret

puts:
    pusha ; snapshot for state restoration (all)

    mov eax, 4
    mov ebx, 1
    int 80h

    popa ; state restoration (all)

    ret

; ------------------------------------
; sprint(
;   ebx : string first address
;) -> void
sprint:
    pusha ; snapshot for state restoration

    call strlen
    mov ecx, ebx ; put the string address into ecx
    mov edx, eax ; put string length in edx
    call puts

    popa

    ret

; ------------------------------------
; sprintLF(
;   ebx : string first address
;) -> void
;
; Prints a string and then prints a LF after it.
; Makes use of the stack to
; simulate a "fake string location" like [0x0A, 0x00].
;
sprintLF:
    ; snapshot for state restoration
    push edx

    ; print our string
    call sprint

    ; 0x0A = 10 is ASCII code for newline
    mov edx, 0x00 ; a nullbyte to terminate LF
    push edx
    mov edx, 0x0A
    push edx

    ; esp will point to 0x0A on stack
    ; esp is decreased everytime something is
    ; pushed onto the stack
    mov ebx, esp
    call sprint

    ; state restoration
    pop edx
    pop edx
    pop edx

    ret


quit:
    mov ebx, 0 ; set exit code
    mov eax, 1 ; set opcode for sys_exit
    int 80h ; call linux interrupt
    ret
