#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num= int(input('digite um numero'))
if (num%2)==1:
    print('o numero {} é impar'.format(num))
else:
    print('o numero {} é par'.format(num))
