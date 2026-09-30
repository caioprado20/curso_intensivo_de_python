minhas_comidas = []
minhas_comidas.append("peixe")
minhas_comidas.append("lasanha")
minhas_comidas.append("x-tudo")
minhas_comidas.append("picadinho")
minhas_comidas.append("refrigerante")
minhas_comidas.append("pizza")

print(f'As minhas três comida favorias são{minhas_comidas[0:3]}')
print(f'ja a minha quarta comida favorita é {minhas_comidas[3:4]}')
print(f"As minhas duas ultimas comidas favoritas são : {minhas_comidas[-2:]}")


thais_food = minhas_comidas[:]
thais_food.append("sorvete")
thais_food.append("Camarão")
thais_food.remove("picadinho")
thais_food.remove("x-tudo")
thais_food.reverse()
print("minhas comidas favoritas são:")
for minhas in minhas_comidas:
    print(minhas)
print("As comidas do mozão são: ")
for mozão in thais_food:
    print(mozão)