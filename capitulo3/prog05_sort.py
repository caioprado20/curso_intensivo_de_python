# Como instanciar uma lista de carros
cars = ['gol', 'c3', 'nirvus', 'toyota']
print(cars)

# Como ordenar a lista em ordem alfabética de forma permanente (sort)
cars.sort()
print(cars)

# Como ordenar a lista em ordem alfabética inversa de forma permanente
cars.sort(reverse=True)
# Nota: \n cria uma nova linha na impressão
print(f'Essa é a lista invertida:\n{cars}')

# Como exibir uma lista ordenada temporariamente sem alterar a lista original (sorted)
print(f'Essa é a lista temporariamente organizada: {sorted(cars)}')

# Como inverter a ordem atual dos elementos da lista (reverse)
cars.reverse()
print(cars)

# Como obter a quantidade de elementos de uma lista usando a função len()
print(len(cars))