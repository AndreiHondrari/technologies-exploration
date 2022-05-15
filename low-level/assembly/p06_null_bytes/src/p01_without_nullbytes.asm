; the idea is that if you don't terminate the string with a nullbyte
; the printing function will just continue
; until illegal memory is being accessed or a random 0x00.
; this is potentiall problematic because it can result in a SIGSEGV crash


%include 'src/functions.asm'

section .data
    msg1 db 'Hello includes!', 0Ah ; 0x0A = 10 is ASCII code for newline
    msg2 db 'Potatoes are life and blood ...', 0Ah

section .text
    global _start

_start:

    mov eax, msg1 ; set string address arg
    call sprint

    mov eax, msg2 ; set string address arg
    call sprint

    ; exiting normally
    call quit
