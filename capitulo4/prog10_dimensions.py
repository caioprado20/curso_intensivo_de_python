### TUPLAS 

# Tupla é um lista que não pode ser modificada depois da sua instaciação
# As tuplas são iniciadas pelo uso de parentese ao inves de colchetes 

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# Se tentarmos modificar seus elementos o python reforna com um erro

# dimensions[0] = 250 // TypeError: 'tuple' object does not support item assignment

# O que define em termos técnicos a tuplas são os usos de vírgula, os parênteses são para facilitar a leitura do valores

dimensions2 = 200,202
print(dimensions2)

### PERCORRENDO OS VALORES DE UMA TUPLA COM UM LOOP
#
# Podemos usa o for para percorrer uma tupla da mesmo forma que com usamos nas listas.

for dimension in dimensions:
    print(dimension)

### SOBRESCREVENDO UMA TUPLA 
#
# Mesmo não sendo possível modificar uma tupla, podes atibuir a uma variável que represente uma tupla.

# Atribuindo a primeira tupla
dimension3 = (200, 50)
print("Original dimensions:")
for dimension in dimension3:
    print(dimension)

# Reatribuindo uma nova tupla à mesma variável
dimension3 = (400, 100)
print("\nModified dimensions:")
for dimension in dimension3:
    print(dimension)