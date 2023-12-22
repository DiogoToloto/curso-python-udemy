"""
Formatação básica de string
s - string
d - int
f - float
.<numero de digitos>f
x ou X - HEXADECIMAL
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita 
^ - centro
"=" força o numero a aparecer antes do zeros
Sinal - + ou -
Ex. : 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:>10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.48399048509385903840:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')