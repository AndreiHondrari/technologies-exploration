; ####################################
; MEMORY
; ####################################

%ifndef ASMLIB_MEMORY
%define ASMLIB_MEMORY

; ------------------------------------
; malloc(
;   eax : size
; ) ->
;   eax : new memory address or errno
;
malloc:
    push ebx
    push ecx
    push edx
    push esi
    push edi
    push ebp

    mov ecx, eax    ; length

    mov eax, 192    ; sys_mmap2 opcode (0xC0)
    mov ebx, 0      ; address = NULL
    mov edx, 1      ; proto = 1 (read)
    or edx, 2       ; proto = 1 | 2 (read and write)
    mov esi, 0x02   ; flags = 2 (map_private)
    or esi, 0x20    ; flags = 2 | 32 (map_private | map_anonymous)
    mov edi, -1     ; file descriptor (requiredd by map_anonymous)
    mov ebp, 0      ; offset = 0
    int 0x80        ; syscall

    pop ebp
    pop edi
    pop esi
    pop edx
    pop ecx
    pop ebx
    ret

%endif ASMLIB_MEMORY
