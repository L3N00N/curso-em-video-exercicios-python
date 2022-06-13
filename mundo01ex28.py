from random import randint
lista= randint(0, 5)
escolhido= int(input('digite um numero entre 0 e 5'))
print('o numero escolhido foi {}'.format(escolhido))
if lista==escolhido:
    print('parabens você acertou o numero')
else:
    print('você errou')
print(lista)
