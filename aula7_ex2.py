nome = input('Digite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
idade = input('Digite a sua idade: ')
altura = input('Sua altura: ')

altura1 = float(altura)
idade1 = int(idade)

if idade1 >= 18:
    print(f'Seu nome é: {nome}')
    print(f'Seu sobrenome: {sobrenome}')
    print(f'Sua idade: {idade}')
    print(f'Você nasceu em {2023 - idade1}')
   
else:
    print('Você não é maior de idade')