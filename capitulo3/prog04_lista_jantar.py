lista_jantar = []
lista_jantar.append('Juliana')
lista_jantar.append('thais')
lista_jantar.append('leticia')
lista_jantar.append('mamãe')
print(f'olá {lista_jantar[0]}  gostaria de jantar comigo sexta a noite:')
print(f'olá {lista_jantar[1]}  gostaria de jantar comigo sexta a noite:')
print(f'olá {lista_jantar[2]}  gostaria de jantar comigo sexta a noite:')
print(f'olá {lista_jantar[3]}  gostaria de jantar comigo sexta a noite:')
print("----------------------------------------------------------------")
del lista_jantar[0]
lista_jantar.insert(0, 'naiana')
print(f'olá {lista_jantar[0]}  gostaria de jantar comigo sexta a noite:')
print(lista_jantar)
print('Opa, consguir uma mesa maior')
lista_jantar.insert(1,'jose')
lista_jantar.append('Luna')
print(f'olá {lista_jantar[1]}  gostaria de jantar comigo sexta a noite:')
print(f'olá {lista_jantar[5]}  gostaria de jantar comigo sexta a noite:')
print("----------------------------------------------------------------")
print('Infelizmente a mesa não vai ficar pronta a tempo e tive que reduzir o numero de convites')
lista_jantar_removidos = []
lista_jantar_removidos.append(lista_jantar.pop() )
lista_jantar_removidos.append(lista_jantar.pop() )
lista_jantar_removidos.append(lista_jantar.pop() )
print(f'infelizmente {lista_jantar_removidos}, não haverar mesas para vcs fica para a proxima')
print(f'{lista_jantar} vamos jantar')
del lista_jantar[2]
del lista_jantar[1]
del lista_jantar[0]


print(lista_jantar)

