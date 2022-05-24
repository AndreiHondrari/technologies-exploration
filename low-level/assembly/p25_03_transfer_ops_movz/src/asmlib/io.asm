; ####################################
; I/O
; ####################################

%ifndef ASMLIB_IO
%define ASMLIB_IO

%include 'src/asmlib/numbers.asm'
%include 'src/asmlib/string.asm'
%include 'src/asmlib/process.asm'

SECTION .data
STACK_BITS_OFFSET equ 4

SECTION .bss

; it takes 10 bytes to display 4.294.967.295 (0x FF FF FF FF)
print_digits_count: resd 1
print_digits: resb 10
print_char_array: resb 11 ; 10 + 1 byte for 0x00

SECTION .text

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
; iprint (
;   eax : integer to display
; )
;
; Prints a number
iprint:
    ; snapshot registers
    push eax
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

    mov byte [print_char_array+ecx], 0x00

    ; print digits
    mov eax, print_char_array
    call sprint

    ; restore registers
    pop esi
    pop edi
    pop ecx
    pop eax
    ret

; ------------------------------------
; iprintLF (
;   eax : integer to display
; )
;
; Prints a number and a linefeed
iprintLF:
    call iprint
    call printLF
    ret

; ------------------------------------
; print_stack_integers (
;   ecx : the number of integers to print from the stack
; )
;
; Print integers pushed to the stack
print_stack_integers:
    ; snapshot registers
    push eax
    push ebx
    push ecx
    push esi

    ; first we must point esi to the address in the stack
    ; of the first argument, because when we do the
    ; snapshot pushes it will push our args further into the stack
    ; so we need a base reference for the first argument
    mov eax, STACK_BITS_OFFSET
    mov ebx, 5 ; the number of registers + the return address
    mul ebx ; calculate the offset from esp in bits

    ; calculate the address of the first available argument in the stack
    mov esi, esp ; copy original esp
    add esi, eax ; add offset on top of the original esp

    .printInteger:
        mov eax, ecx ; copy current stack pointer index offset

        ; offset the stack pointer index offset with -1
        ; (1 .. n) -> (0 .. n-1)
        sub eax, 1
        mov ebx, STACK_BITS_OFFSET ; copy the stack bits offset
        mul ebx ; determine our actual offset in bits
        mov ebx, eax ; copy the bits offset to ebx

        mov eax, [esi+ebx] ; copy the value from the stack with offset
        call iprintLF

        dec ecx
        cmp dword ecx, 0
        jz .endPrintInteger
        jmp .printInteger

    .endPrintInteger:

    ;restore registers
    pop esi
    pop ecx
    pop ebx
    pop eax
    ret

%endif
