# Calculadora com while

while True:
    numero1 = input('Digite um numero: ')
    numero2 = input('Digite outro numero: ')
    operador = input('Digite o operador(+-/*): ')

    numeros_validos = None
    numero1_float = 0
    numero2_float = 0

    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numeros_validos = True
        
    except:
        numeros_validos = None

    if numeros_validos is None:
            print('Um ou ambos os numeros são invalidos.')
            continue
 
    opedores_validos = '+-/*'

    if operador not in opedores_validos:
            print('Operador invalido.')
            continue

    if len(operador) > 1:
            print('Digite apenas um operador.')
            continue

    print('Realizando sua conta, confira o resultado abaixo.')

    if operador == '+':
          print(f'{numero1_float}+{numero2_float}:',numero1_float + numero2_float)
    elif operador == '-':
          print(f'{numero1_float}-{numero2_float}:',numero1_float - numero2_float)
        
    elif operador == '/':
          print(f'{numero1_float}/{numero2_float}:',numero1_float / numero2_float)
          
    elif operador == '*':
          print(f'{numero1_float}*{numero2_float}:',numero1_float * numero2_float)
          

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
   
    if sair is True:
        break