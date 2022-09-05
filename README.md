![git status](http://3.129.230.99/svg/cemmanuelsr/compiler/)

# Compiler

## Diagrama Sintático

![diagrama](assets/img/diagrama-sintatico.jpg)

## EBNF

```
<number> ::= [0-9]+

<operator> ::= +
             | -
             | *
             | /
             
<term> ::= <number>
         | <term> * <number>
         | <term> / <number>
        
<expression> ::= <term>
               | <expression> + <term>
               | <expression> - <term>
```
