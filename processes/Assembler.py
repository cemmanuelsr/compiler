class Assembler:
    header = '''; constantes
    SYS_EXIT equ 1
    SYS_READ equ 3
    SYS_WRITE equ 4
    STDIN equ 0
    STDOUT equ 1
    True equ 1
    False equ 0
    
    segment .data
    
    segment .bss  ; variaveis
      res RESB 1
    
    section .text
      global _start
    
    print:  ; subrotina print
    
      PUSH EBP ; guarda o base pointer
      MOV EBP, ESP ; estabelece um novo base pointer
    
      MOV EAX, [EBP+8] ; 1 argumento antes do RET e EBP
      XOR ESI, ESI
    
    print_dec: ; empilha todos os digitos
      MOV EDX, 0
      MOV EBX, 0x000A
      DIV EBX
      ADD EDX, '0'
      PUSH EDX
      INC ESI ; contador de digitos
      CMP EAX, 0
      JZ print_next ; quando acabar pula
      JMP print_dec
    
    print_next:
      CMP ESI, 0
      JZ print_exit ; quando acabar de imprimir
      DEC ESI
    
      MOV EAX, SYS_WRITE
      MOV EBX, STDOUT
    
      POP ECX
      MOV [res], ECX
      MOV ECX, res
    
      MOV EDX, 1
      INT 0x80
      JMP print_next
    
    print_exit:
      POP EBP
      RET
    
    ; subrotinas if/while
    binop_je:
      JE binop_true
      JMP binop_false
    
    binop_jg:
      JG binop_true
      JMP binop_false
    
    binop_jl:
      JL binop_true
      JMP binop_false
    
    binop_false:
      MOV EBX, False
      JMP binop_exit
    binop_true:
      MOV EBX, True
    binop_exit:
      RET
    
    _start:
    
      PUSH EBP ; guarda o base pointer
      MOV EBP, ESP ; estabelece um novo base pointer
    
      ; codigo gerado pelo compilador
    '''
    body = ''
    footer = '''; interrupcao de saida
      POP EBP
      MOV EAX, 1
      INT 0x80
    '''

    @staticmethod
    def _restart():
        Assembler.body = ''

    @staticmethod
    def write(filename: str = 'example.asm', path: str = 'assets/asm'):
        content = Assembler.header + '\n' + Assembler.body + '\n' + Assembler.footer
        cleaned_content = '\n'.join([line.strip() for line in content.split('\n')])
        with open(f'{path}/{filename}.asm', 'w+') as file:
            file.write(cleaned_content)
        Assembler._restart()

