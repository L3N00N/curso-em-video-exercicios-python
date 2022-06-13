#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
lista= randint(0, 5)
escolhido= int(input('digite um numero entre 0 e 5'))
print('o numero escolhido foi {}'.format(escolhido))
if lista==escolhido:
    print('parabens você acertou o numero')
else:
    print('você errou')
print(lista)
