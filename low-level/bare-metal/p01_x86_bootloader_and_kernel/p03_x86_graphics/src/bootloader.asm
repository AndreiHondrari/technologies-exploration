org 0x7C00 ; address of reference for indexing

; reset disk position

mov ah,0
int 0x13

; read the kernel from hard-drive and copy to RAM

; bootloader is at segment 0 (exactly 512 bytes)

mov bx, 0x8000 ; select free memory starting address

; AX | 0x02 | 0x01 |
; CX | 0x00 | 0x02 |
; DX | 0x00 | ---- |
mov al, 1 ; amount of sectors to read (1 x 512 bytes)
mov ah, 2 ; 0x02 read from disk (secondary opcode)

mov cl, 2 ; sector = 2 (bootloader = 1, kernel = 2)
mov ch, 0 ; cylinder/track = 0 (first out of 2)
mov dh, 0 ; head = 0 (first 18 sectors)

int 0x13

; final bootloader instructions

jmp 0x8000 ; set next instruction to beginning of kernel

; pad everything from last bootloader byte
; to 510 with 0x00
; $ = address at current position
; $$ = address for start of segment
; declare byte 0x00
times 510-($-$$) db 0

; times is a NASM pseudo-instruction
; used by the compiler
; when generating the binary

; declare MBR ending signature

db 0x55 ; byte 511 = 0x55
db 0xAA ; byte 512 = 0xAA
