
; -------------------------------------
; quits program
quit:
    mov ebx, 0 ; set exit code
    mov eax, 1 ; set opcode for sys_exit
    int 80h ; call linux interrupt
    ret

; -------------------------------------
; quits program with error code 1
error:
    mov ebx, 1 ; set exit code
    mov eax, 1 ; set opcode for sys_exit
    int 80h ; call linux interrupt
    ret

; -------------------------------------
; strlen(
;   eax : string address
; ) -> eax : string size
;
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
; sprint (
;   eax : string address message
; )
;
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
; printLF ()
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
; sprintLF (
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
; getinput (
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
; bappend (
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
; bcopy (
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

; ------------------------------------
; dtoascii (
;   eax : the numeric digit to convert to ASCII code
; ) -> eax : ASCII code of the input digit
;
; Convert a numeric digit to ASCII code
dtoascii:
    cmp eax, 0
    jl .nonDigitException
    cmp eax, 9
    jg .nonDigitException

    add eax, 0x30
    ret

    .nonDigitException:
        mov eax, non_digit
        call sprintLF
        call printLF
        call error

; ------------------------------------
; itoa (
;   eax : address of the input number,
;   edi : address of the output buffer
; ) ->
;   ecx : number of digits placed in the buffer
;
; Extracts digits from a number and places them in a buffer
itoa:
    ; snapshot registers
    push eax
    push ebx
    push edx

    mov ebx, 10 ; set divisor
    mov ecx, 0 ; set loop (digits) counter

    ; extract individual digits
    .extractDigit:
        cmp eax, 0 ; determine if we don't have any digits left
        jz .endExtractDigits

        mov edx, 0
        div ebx ; get rightmost digit (stored in EDX)
        push edx ; stack digit

        inc ecx
        jmp .extractDigit

    .endExtractDigits:

    ; temporarily store digits count in variable
    mov [itoa_digits_count], ecx

    ; transfer digits to buffer
    mov eax, 0 ; reset eax
    mov ecx, 0
    .transferDigit:
        ; check if we transfered all digits
        cmp ecx, [itoa_digits_count]
        jge .endTransferDigits

        pop eax ; pop a digit from the stack
        mov byte [edi+ecx], al ; write the digit to the buffer

        inc ecx ; count our transfered digit
        jmp .transferDigit

    .endTransferDigits:

    ; restore registers
    pop edx
    pop ebx
    pop eax
    ret

; ------------------------------------
; convert_digits_to_ascii (
;   esi : source buffer address,
;   edi : destination buffer address,
;   ecx : number of digits to convert
; )
;
; Convert digits to ASCII codes
; from one buffer to another
convert_digits_to_ascii:
    push eax
    push ecx

    ; load args
    mov [convert_digits_count], ecx

    mov eax, 0
    mov ecx, 0
    .convertDigit:
        cmp dword ecx, [convert_digits_count]
        jge .endConvertDigits

        mov byte al, [esi+ecx]
        call dtoascii
        mov byte [edi+ecx], al

        inc ecx
        jmp .convertDigit
    .endConvertDigits:

    pop ecx
    pop eax
    ret

; ------------------------------------
; print_integer (
;   eax : integer to display
; )
;
; Prints a number
print_integer:
    ; snapshot registers
    push ecx
    push edi
    push esi

    ; generate array of digits from a given integer
    mov edi, print_digits
    call itoa
    mov dword [print_digits_count], ecx

    ; convert all digits to ASCII codes
    mov esi, print_digits
    mov edi, print_char_array
    call convert_digits_to_ascii

    inc ecx
    mov byte [print_char_array+ecx], 0x00

    ; print digits
    mov eax, print_char_array
    call sprintLF

    ; restore registers
    pop esi
    pop edi
    pop ecx
    ret

SECTION .data
non_digit db 'Error! EAX not single digit for dtoascii operation', 0x00

SECTION .bss
itoa_digits_count: resd 1
convert_digits_count: resd 1

; it takes 10 bytes to display 4.294.967.295 (0x FF FF FF FF)
print_digits_count: resd 1
print_digits: resb 10
print_char_array: resb 10
