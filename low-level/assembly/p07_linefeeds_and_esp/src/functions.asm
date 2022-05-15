
; -------------------------------------
; quits program
quit:
    mov ebx, 0 ; set exit code
    mov eax, 1 ; set opcode for sys_exit
    int 80h ; call linux interrupt
    ret

; -------------------------------------
; strlen(
;   eax : string address
; ) -> eax : string size
; Calculates the size of the string
strlen: ; define the strlen subroutine
    ; snapshot for state restoration
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
; puts(
;   eax : string address,
;   ebx : string size
; )
puts:
    ; snapshot for state restoration
    push eax
    push ebx

    ; load args
    mov ecx, eax ; set string address
    mov edx, ebx ; set string size

    mov eax, 4 ; set sys_write opcode
    mov ebx, 1 ; set filedescriptor to STDOUT=1
    int 80h ; call linux interrupt

    ; state restoration
    pop ebx
    pop eax
    ret

; -------------------------------------
; sprint(
;   eax : string address message
; )
; Calculates the size of the string and prints it
sprint:
    ; snapshot for state restoration
    push eax
    push ebx
    push ecx

    ; load args
    mov ecx, eax ; ecx as temporary register for string address mem

    call strlen ; obtain the string size in EAX

    mov ebx, eax ; set the string size arg
    mov eax, ecx ; set the string address arg
    call puts ; print the string

    ; state restoration
    pop ecx
    pop ebx
    pop eax
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
    push eax

    call sprint

    mov eax, 0x0A
    push eax ; memorize the LF character onto the stack
    mov eax, esp
    call sprint

    pop eax ; remove the LF character from the stack

    ; state restoration
    pop eax
    ret
