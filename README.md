![git status](http://3.129.230.99/svg/cemmanuelsr/compiler/)

# Compiler

Um compilador desenvolvido em Python para a linguagem Carbon.

## Diagrama Sintático

![diagrama sintatico](assets/img/diagrama-sintatico.svg)

## EBNF

```
PROGRAM = { DECLARATION } ;
DECLARATION = "fn", IDENTIFIER, "(", ( "" | ARGUMENT, { ",", ARGUMENT } ), ")", ( "" | "->", TYPE ), BLOCK ;
ARGUMENT = IDENTIFIER, { "," }, ":", TYPE ;
BLOCK = "{", { STATEMENT }, "}" ;
STATEMENT = (( λ | ASSIGNMENT | PRINT | ("var", IDENTIFIER, {",", IDENTIFIER}, ":", TYPE) ), ";" | ( LOOP | CONDITION | BLOCK ) | "return" REL_EXPRESSION ) ;
ASSIGNMENT = IDENTIFIER, "=", REL_EXPRESSION ;
PRINT = "Print", "(", REL_EXPRESSION, ")" ;
LOOP = "while", "(", REL_EXPRESSION, ")", STATEMENT ;
CONDITION = "if", "(", REL_EXPRESSION, ")", STATEMENT, ( λ | "else", STATEMENT ) ;
REL_EXPRESSION = EXPRESSION, { ("==" | ">" | "<" | "."), EXPRESSION } ;
EXPRESSION = TERM, { ("+" | "-" | "||"), TERM } ;
TERM = FACTOR, { ("*" | "/", "&&"), FACTOR } ;
FACTOR = (("+" | "-" | "!"), FACTOR) | NUMBER | "(", EXPRESSION, ")" | IDENTIFIER, ( "" | "(", ( "" | REL_EXPRESSION, { ",", REL_EXPRESSION } ), ")" ) | "Read", "(", ")" ;
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
NUMBER = DIGIT, { DIGIT } ;
LETTER = ( a | ... | z | A | ... | Z ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
TYPE = ( "String" | "i32" ) ;
```

## Visualização

O script main também gera um arquivo em linguagem DOT que pode ser usado para visualizar a AST do código.

Você pode desenhá-lo usando o software que desejar ou, caso possua graphviz instalado, executar o script `draw.py` e desenhar a AST como essa abaixo que calcula os 102 primeiros termos da sequência de Fibonacci:

![exemplo AST](assets/img/fibonacci.svg)
