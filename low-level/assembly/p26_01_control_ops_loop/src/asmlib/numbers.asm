; ####################################
; NUMBERS
; ####################################

%ifndef ASMLIB_NUMBERS
%define ASMLIB_NUMBERS

SECTION .bss
itoa_digits_count: resd 1

SECTION .text

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
    push edi

    mov ecx, 0 ; set loop (digits) counter

    cmp eax, 0
    jnz .extractNonZero
    mov byte [edi+ecx], 0
    mov ecx, 1

    jmp .itoaEnd

    .extractNonZero:

    mov ebx, 10 ; set divisor

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

    .itoaEnd:
    ; restore registers
    pop edi
    pop edx
    pop ebx
    pop eax
    ret

%endif
