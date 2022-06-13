#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
nome_cidade= str(input('digite o nome de uma cidade')).strip().lower()
nome = 'santo' in nome_cidade
print(nome)
