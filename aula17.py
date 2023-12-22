# Operadores lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras.
# se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# são considerados falsy (que você já viu)
# 0 / 0.0 / '' False
# também existe o tipo none que é
# usado para representar uma valor inexistente

#entrada = input('[E]ntrar[S]air:')
#senha_digitada = input('Senha: ')

#senha_permitida = "123456"
#if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#    print('Entrar')
#else:
#    print('Sair')

senha = input("Senha: ") or 'Sem senha'
print(senha)

