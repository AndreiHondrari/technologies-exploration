org 0x8000
bits 16

section .data
    col dw 0
    row dw 0
    color dw 0

section .text
    global main

main:
    ; main call

    ; set video mode

    mov al, 0x13 ; video mode 0x13 = 320x200 with 256 colors
    mov ah, 0x00 ; set secondary opcode as 0x00 = "set video mode"
    int 0x10 ; call video service opcode

    call drawToScreen

    ; ending call
    jmp $
    hlt
    ret

    ; functions

drawMulticolorLine:
    mov word [row], 50

    .rowLoop:
        mov cx, 60
        mov dx, 0

        .colLoop:
            push dx

            mov ah, 0xC ; secondary opcode for "set graphic pixel"
            mov bh, 0 ; page
            mov al, dl ; color
            mov dx, word [row] ; row
            int 0x10 ; call video service opcode

            pop dx
            inc dx
            cmp dx, 0x00FF
            jle .skipColorReset
            mov dx, 0
            .skipColorReset:

            inc cx
            cmp cx, 260
            jge .colSkip

            jmp .colLoop

        .colSkip:

        inc word [row]
        cmp word [row], 150
        jge .rowSkip

        jmp .rowLoop

    .rowSkip:

    ret

drawToScreen:
    call drawMulticolorLine
    ret

; padding
times 512-($-$$) db 0
