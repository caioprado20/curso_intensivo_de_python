# Como instanciar uma lista
lista1 = ['honda', 'yamaha', "suzuki"]
print(lista1)
print("--------------------------------------------")

# Como substituir um elemento pelo seu índice
lista1[0] = 'ducati'
print("--------------------------------------------")

print(lista1)

# Como instanciar uma nova lista
lista2 = ['honda', 'yamaha', "suzuki"]

# Como adicionar um elemento ao final da lista (append)
lista2.append('ducati')
print(lista2)
print("--------------------------------------------")

# Como instanciar uma lista vazia
lista3 = []
print("--------------------------------------------")

# Como adicionar elementos sequencialmente ao final de uma lista vazia
lista3.append('CG')
lista3.append('biz')
lista3.append('cross')
print(lista3)
print("--------------------------------------------")

# Como inserir um elemento em uma posição específica (insert)
lista3.insert(0, 'Titan')
print(lista3)
print("--------------------------------------------")

# Como deletar um elemento pelo seu índice usando a palavra-chave del
del lista1[0]
print(lista1)
print("--------------------------------------------")

# Como remover o último elemento de uma lista usando pop()
lista1.pop()
print(lista1)
print("--------------------------------------------")

# Como remover o último elemento e armazenar seu valor em uma variável
popend_lista2 = lista2.pop()
print(lista2)
print(popend_lista2)
print("--------------------------------------------")

# Como remover o último elemento e formatar com o método title() em uma f-string
ultima_compra = lista3.pop()
print(f"A ultima moto comprada do estoque foi {ultima_compra.title()}")
print("--------------------------------------------")

# Como remover um elemento pelo seu valor (remove)
lista2.remove("yamaha")
print(lista2)
print("--------------------------------------------")

# Como armazenar o valor em uma variável antes de remover da lista por esse valor
muito_cara = 'suzuki'
lista2.remove("suzuki")
print(f'a moto {muito_cara} tem um valor muito alto para mim.')
print("--------------------------------------------")

