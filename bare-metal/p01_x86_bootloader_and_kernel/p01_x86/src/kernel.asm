org 0x8000
bits 16
mov si, msg
call printNullTerminatedString

jmp $
hlt
ret

printCharacter:
    mov ah, 0x0E

    mov bl, 0x00
    mov bh, 0x00

    int 0x10
    ret

printNullTerminatedString:
    pusha

    .loop:
        lodsb
        test al, al
        jz .end
        call printCharacter

    jmp .loop

    .end:
        popa
        ret

msg db "Czesc mundo!"
times 512-($-$$) db 0
