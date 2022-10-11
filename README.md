![git status](http://3.129.230.99/svg/cemmanuelsr/compiler/)

# Compiler

## Diagrama Sintático

![diagrama sintatico](assets/img/diagrama-sintatico.svg)

## EBNF

```
BLOCK = "{", { STATEMENT }, "}" ;
STATEMENT = (( λ | ASSIGNMENT | PRINT ), ";" | ( LOOP | CONDITION | BLOCK )) ;
ASSIGNMENT = IDENTIFIER, "=", REL_EXPRESSION ;
PRINT = "Print", "(", REL_EXPRESSION, ")" ;
LOOP = "while", "(", REL_EXPRESSION, ")", STATEMENT ;
CONDITION = "if", "(", REL_EXPRESSION, ")", STATEMENT, ( λ | "else", STATEMENT ) ;
REL_EXPRESSION = EXPRESSION, { ("==" | ">" | "<"), EXPRESSION } ;
EXPRESSION = TERM, { ("+" | "-" | "||"), TERM } ;
TERM = FACTOR, { ("*" | "/", "&&"), FACTOR } ;
FACTOR = (("+" | "-" | "!"), FACTOR) | NUMBER | "(", EXPRESSION, ")" | IDENTIFIER | "Read", "(", ")" ;
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
NUMBER = DIGIT, { DIGIT } ;
LETTER = ( a | ... | z | A | ... | Z ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
```
