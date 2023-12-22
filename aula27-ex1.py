"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = ''

while not entrada.isdigit():

    entrada = input('Digite um numero inteiro: ')

if entrada.isdigit():
    entrada = int(entrada)
    par_impar = entrada % 2 == 0
    par_impar_texto = 'não informado'

    if par_impar:
        par_impar_texto = 'par'

        print(f'O numero {entrada} é {par_impar_texto}')

    else:
        par_impar_texto = 'ímpar'

        print(f'O numero {entrada} é {par_impar_texto}')

else:
    print('Esse numero não é inteiro')