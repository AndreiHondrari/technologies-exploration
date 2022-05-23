; ####################################
; ARRAY
; ####################################

%ifndef ASMLIB_ARRAY
%define ASMLIB_ARRAY

%include 'src/asmlib/binary.asm'

; ------------------------------------
; array_get(
;   eax : array starting address,
;   ebx : buffer address where to store the value,
;   ecx : index in the array,
;   edx : value size (in bytes)
; )
;
; Get the value from a specific index and store it in a buffer
array_get:
    pusha

    mov esi, eax ; store the starting array address (as source)

    push eax ; stack array address
    push ebx ; stack buffer address
    push ecx ; stack the index
    push edx ; stack the value size

    ; calculate the offset for esi in full value size
    mov eax, ecx
    mov ebx, edx
    mul ebx ; eax will be index * value size
    add esi, eax ; offset the array address by index * value size

    pop edx ; restore the value size
    pop ecx ; restore the index
    pop ebx ; restore buffer address
    pop eax ; restore array address

    ; proceed with the data copy
    mov edi, ebx ; store our buffer destination in edi
    mov ebx, edx ; specify the number of byte to copy
    call bcopy ; copy the value into the buffer

    popa
    ret

; ------------------------------------
; array_set(
;   eax : array starting address,
;   ebx : buffer address where to copy the value from,
;   ecx : index in the array,
;   edx : value size (in bytes)
; )
;
; Set the value from a specific buffer and store it
; into the array at a given index location
array_set:
    pusha

    mov edi, eax ; store the starting array address (as dest)

    push eax ; stack array address
    push ebx ; stack buffer address
    push ecx ; stack the index
    push edx ; stack the value size

    ; calculate the offset for edi in full value size
    mov eax, ecx
    mov ebx, edx
    mul ebx ; eax will be index * value size
    add edi, eax ; offset the array address by index * value size

    pop edx ; restore the value size
    pop ecx ; restore the index
    pop ebx ; restore buffer address
    pop eax ; restore array address

    ; proceed with the data copy
    mov esi, ebx ; store our buffer source in esi
    mov ebx, edx ; specify the number of bytes to copy
    call bcopy ; copy the value into the buffer

    popa
    ret


%endif
