#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome= str(input('digite seu nome'))
dividido= nome.split()
nome1= dividido[0:1]
nome2= dividido[-1:]
print(nome1)
print(nome2)
