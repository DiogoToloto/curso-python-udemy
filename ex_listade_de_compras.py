'''
Faça uma lista de comprar com listas
O usuario deve ter a posibilidade de
inserir, apagar e listar valores da sua lista
não permita que o programa quebre com erros
de indices inexistentes na lista.
'''
import os

lista = []

while True:
    
    print('Selecione uma opção')
    entrada = input('[i]nserir [a]pagar [l]istar:')

    if entrada == 'inserir' or entrada == 'i':
        os.system('cls')
        valor = input('Digite o valor:')
        lista.append(valor)
        os.system('cls')

    elif entrada == 'apagar' or entrada == 'a':
        os.system('cls')
        valorApagar = input('Escolha o índice para apagar:')

        try:
            indice = int(valorApagar)
            del lista[indice]
        except ValueError:
            print('Por favor digite um número inteiro')
        except IndexError:
            print('Indice não existe na lista')

    elif entrada == 'listar' or entrada == 'l':
        os.system('cls')
        indices = range(len(lista))

        for i in indices:
            print(i, lista[i])