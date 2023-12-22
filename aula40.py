"""
append = adiciona um item no final da lista
insert = adiciona um item no indice escolhido
pop = removo do final sem escolher um indice, 
ou qualquer um escolhendo o indice
del = apaga um indice
clear = limpa a lista
extend = estende a lista
+ = concatena listas
create read update delete
criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0  1  2  3
lista = [10,20,30,40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
#lista.clear()
lista.insert(0, 5)
print(lista)