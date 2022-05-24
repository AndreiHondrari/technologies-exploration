; ####################################
; STRING
; ####################################

%ifndef ASMLIB_STRING
%define ASMLIB_STRING

SECTION .data
non_digit db 'Error! EAX not single digit for dtoascii operation', 0x00

SECTION .bss
convert_digits_count: resd 1

SECTION .text

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

%endif
