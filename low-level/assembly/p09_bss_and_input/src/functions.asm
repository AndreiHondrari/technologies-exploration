
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

    mov eax, 4 ; linux sys_write opcode
    mov ebx, 1 ; write to STDOUT file
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
; printLF() -> void
;
; Makes use of the stack to
; simulate a "fake string location" like [0x0A, 0x00].
; uses esp to print
printLF:
    push ebx
    push edx

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

    pop edx ; pop the 0x0A
    pop edx ; pop the 0x00
    pop edx ; restore original edx
    pop ebx ; restore original ebx
    ret

; ------------------------------------
; sprintLF(
;   ebx : string first address
;) -> void
;
; Prints a string and then prints a LF after it.
sprintLF:
    call sprint ; print our string
    call printLF ; print LF
    ret


; ------------------------------------
; getinput(
;   eax: address of buffer to save input to
;   exd: length of the output buffer
;)
getinput:
    pusha

    mov ecx, eax ; eax holds our variable address initially
    mov eax, 0x03 ; 0x03 = opcode for sys_read
    mov ebx, 0 ; STDIN = 1
    int 80h

    popa
    ret

quit:
    mov ebx, 0 ; set exit code
    mov eax, 1 ; set opcode for sys_exit
    int 80h ; call linux interrupt
    ret
