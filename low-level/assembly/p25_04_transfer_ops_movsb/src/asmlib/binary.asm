; ####################################
; BINARY
; ####################################

%ifndef ASMLIB_BINARY
%define ASMLIB_BINARY

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

%endif
