
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
; swrite(
;   eax : string address,
;   ebx : string size
; )
swrite:
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
    call swrite ; print the string

    ; state restoration
    pop ecx
    pop ebx
    pop eax
    ret


; ------------------------------------
; printLF() -> void
;
; Prints a new line (linefeed)
printLF:
    ; snapshot for state restoration
    push eax

    mov eax, 0x0A
    push eax ; memorize the LF character onto the stack
    mov eax, esp ; set esp address as string address
    call sprint

    pop eax ; remove the LF character from the stack

    ; state restoration
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
    call sprint
    call printLF
    ret


; ------------------------------------
; getinput(
;   eax: address of buffer to save input to
;   exd: length of the output buffer
;)
getinput:
    ; snapshot for state restoration
    pusha

    ; load from args
    mov ecx, eax ; set buffer address
    mov edx, ebx ; set buffer size

    mov eax, 0x03 ; 0x03 = opcode for sys_read
    mov ebx, 0 ; STDIN = 1
    int 80h

    ; state restoration
    popa
    ret

; ------------------------------------
; bappend(
;   eax: byte to store
;   ebx: buffer address to store byte into
;   edi: index at which to store byte
;) ->
;   edi = edi + 1
;
; Stores a byte at specified edi index and
; then increments the edi
bappend:
    ; snapshot for state restoration
    push eax
    push ebx

    mov byte [ebx+edi], al
    inc edi

    ; state restoration
    pop ebx
    pop eax
    ret

; ------------------------------------
; bcopy(
;   esi : source address,
;   edi : destination address,
;   ebx : number of bytes to copy
; )
;
; Copy a number of bytes from one memory to another
bcopy:
    pusha ; snapshot registers

    mov ecx, 0 ; initialize loop counter

    .copyByte:
        cmp ecx, ebx ; check number of bytes copied so far
        jge .endCopy

        mov byte al, [esi+ecx] ; copy from source to lower AX
        mov byte [edi+ecx], al ; copy to destination from lower AX

        inc ecx ; increment coutner
        jmp .copyByte ; repeat

    .endCopy:

    popa ; restore registers
    ret
