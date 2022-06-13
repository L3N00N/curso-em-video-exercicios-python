#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
nome= input('digite seu nome')
print(nome.upper())
print(nome.lower())
num_caract= (nome.replace(' ', ''))
print(len(num_caract))
nome1= nome.split()
letras1nome=  nome1[0]
print(len(letras1nome))
