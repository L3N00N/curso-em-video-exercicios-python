#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
alun1= str(input('digite o 1º nome'))
alun2= str(input('digite o 2º nome'))
alun3= str(input('digite o 3º nome'))
alun4= str(input('digite o 4º nome'))
lista= [alun1, alun2, alun3, alun4]
print(shuffle(lista))
