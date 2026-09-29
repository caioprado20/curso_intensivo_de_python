### COPIANDO LISTAS

#Com a sintaxe lista = listacopiado[:] é possivel copiar toda uma lista para uma nova

my_foods = ['pizza',' falafel','carrot cake']
friend_foods = my_foods[:]
print(f"My favorite foods are: \n{my_foods}")

print(f"\nMy friend's favorite foods are : \n{friend_foods}")

# Para demostrar  que são duas lista separas, adicionaremos um elemento na primeira lista

my_foods.append("cannoli")
friend_foods.append('ice cream')
print(f"My favorite foods are: \n{my_foods}")

print(f"\nMy friend's favorite foods are : \n{friend_foods}")

# Se simplesmente fizemos uma sintaxe de my_foods = friend'sfood o python não vai criar duas listas e sim a variável friend'sfood será apontada para a lista my_foods e se quisermos adicionar elemento só em uma não será possivel 

friend_foods = my_foods

my_foods.append('Hot-dog')
friend_foods.append('empada')
print(f"My favorite foods are: \n{my_foods}")

print(f"\nMy friend's favorite foods are : \n{friend_foods}")














