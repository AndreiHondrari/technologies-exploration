; ####################################
; PROCESS
; ####################################

%ifndef ASMLIB_PROCESS
%define ASMLIB_PROCESS

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

%endif
