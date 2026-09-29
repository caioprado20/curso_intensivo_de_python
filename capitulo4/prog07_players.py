 # SlICING(FATIA)

 # A sintaxe do slicing(fatia) [inicio :(comando para slicing)termino] os valores do indice
players = ['charles','martina','micheal','florence','eli']
print(players[0:3])

#Mudou o inicio para o indice 1

print (players[1:4])

# Também pode-se omitir o início que o python entenderá como o início seja desde o começo da lista.
print(players[:4])

# Também pode-se omitir o o fim que o python entenderá como o fim seja até o final da lista 

print(players[2:])

# Pode manipular a lista usando os indice negativos para obter a saída do ultimos elementos. No caso abaixo queremos obter os 3 ultimos itens da lista
print(players[-3:])

### SLICING NO LOOP

# Podemos usar o for para percorrer so uma fatia da lista para obtermos so o resultado que queremos sem percorrer a lista toda

print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())

