# # Coleções
# # Tuplas

# nomes = ('Goku', 'Vegeta', 'Trunks', 'Gohan')

# # SELECT
# print(nomes)
# print(nomes[0])
# print(nomes[1:3]) #Slicing - Primeiro elemento inclusive e segundo exclusive

# # INSERT, UPDATE, DELETE
# nomes[0] = 'Picolo'
# print(nomes)

# nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan']

# # SELECT
# print(nomes[2:])

# # INSERT
# nomes.insert(1, 'Freezer')
# print(nomes)
# nomes.append('Kuririn')
# print(nomes)

# # UPDATE
# nomes[0] = 'Bulma'
# print(nomes)

# # DELETE

# nomes.remove('Vegeta')

# del nomes[0]

# print(nomes)

# nomes = {'Goku', 'Vegeta', 'Trunks', 'Gohan'}

# # SELECT
# print(nomes)

# nomes.add('Bulma')
# nomes.add('Goku')

# nomes.remove('Vegeta')

# print(nomes)

# DICIONARIOS

pessoa = {
    'nome': 'Goku', 
    'idade': 40, 
    'sexo': 'M'
}

print(pessoa['idade'])

pessoa['hobby'] = 'comer'

pessoa['nome'] = 'Gohan'

del pessoa['sexo']

print(pessoa)




