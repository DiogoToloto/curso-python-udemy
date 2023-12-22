"""
Operadores in e not in
Strings são iteráveis
 0 1 2 3 4  
 d i o g o
-5-4-3-2-1
"""
#nome = "Diogo"
#print(nome[0])
#print('Dio' in nome)
#print('ga' in nome)
#print( 10 * '-')
#print('Dio' not in nome)
#print('Die' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')