org 0x8000
bits 16

section .data
    minRow dw 80
    maxRow dw 120
    minCol dw 100
    maxCol dw 220

    col dw 0
    row dw 0
    color dw 0
    offset dw 0
    startTicks dw 0
    clockTicks dw 0

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

    .offsetLoop:
        ; mov dx, word [minRow]
        mov dx, 0
        mov word [row], dx

        .rowLoop:
            ; mov cx, word [minCol]
            mov cx, 0
            mov dx, word [offset]

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
                mov dx, word [offset]
                .skipColorReset:

                inc cx
                ; cmp cx, word [maxCol]
                cmp cx, 320
                jge .colEnd

                jmp .colLoop

            .colEnd:

            inc word [row]
            ; mov dx, word [maxRow]
            mov dx, 200
            cmp word [row], dx
            jge .rowEnd

            jmp .rowLoop

        .rowEnd:

        inc word [offset]
        cmp word [offset], 0x00ff
        jle .skipOffsetReset
        mov word [offset], 0
        .skipOffsetReset:

        ; sleep instructions sequence loop

        ; pusha ; save offsetLoop registers
        ;
        ; mov ah, 0x00
        ; int 0x1A ; get first system time
        ;
        ; mov word [startTicks], dx
        ;
        ; .sleepLoop:
        ;
        ;     mov ah, 0x00
        ;     int 0x1A ; get subsequent system time
        ;
        ;     sub dx, word [startTicks]
        ;     mov word [clockTicks], dx
        ;
        ;     cmp word [clockTicks], 1
        ;     jge .sleepLoopEnd
        ;
        ;     jmp .sleepLoop
        ;
        ; .sleepLoopEnd:
        ;
        ; popa ; restore offsetLoop registers

        jmp .offsetLoop

    .offsetEnd:

    ret

drawToScreen:
    call drawMulticolorLine
    ret

; padding
times 512-($-$$) db 0
