![git status](http://3.129.230.99/svg/cemmanuelsr/compiler/)

# Compiler

## Diagrama Sintático

![diagrama](assets/img/diagrama-sintatico.jpg)

## EBNF

```
FACTOR = ("+" | "-") FACTOR | "(" EXPRESSION ")" | number ;
TERM = FACTOR, { ("*" | "/"), FACTOR } ;
EXPRESSION = TERM, { ("+" | "-"), TERM } ;
```