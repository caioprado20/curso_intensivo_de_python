first_name = " Caio"
last_name = " Prado "
full_name =f"{first_name} {last_name}"
message = f"Olar {full_name}, gostaria de aprender Pytohn hoje?"
print(message)
print("Seu nome maiúsculo " + full_name.upper())
print("Seu nome minúsculo " + full_name.lower())
print("Seu nome com as primeiras letras maiúsculas " + full_name.title())
citação = 'O Cabeludo lavador de carros disse o segunte" Ja tive tanto dinheiro na vida e perdi tudo que hj não tenho pressa"'
print(citação)
print(f"O nome quebrando linha: \n{first_name}\n{last_name}")
print(f"O nome quebrando linha e tabulando: \n\t{first_name}\n\t{last_name}")
message = f"Olar '{full_name.rstrip()}', vou tirar o espaço da direita"
print(message)
message = f"Olar '{full_name.lstrip()}', vou tirar o espaço da esquerda"
print(message)
message = f"Olar '{full_name.strip()}', vou tirar todos espaço "
print(message) 

print("###############################################################")

filename = 'python_notes.txt'
print(filename.removesuffix(".txt"))