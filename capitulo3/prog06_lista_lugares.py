lugares = []
lugares.append('Belém')
lugares.append('Macapá')
lugares.append('Marituba')
lugares.append('Vigia')
lugares.append('Cametá')
print(f'Essa é a lista original: \n{lugares}')

print(f'Esta é a lista temporaria ordena alfabeticamente: \n{sorted(lugares)}')

print(f'Novamente a lista original sem alterações: \n{lugares}')

lugares.reverse()

print(f'Lista reversa\n{lugares}')

lugares.reverse()

print(f'Lista revertia novamente, logo, de volta ao estado original \n{lugares}')
lugares.sort()
print(f'Agora a lista permanentimente modificada \n{lugares}')

print(f'Quantidade de lugares presentes na lista {len(lugares)}')