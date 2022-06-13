#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase= str(input('digite uma frase').upper().replace(' ', ''))
frase2= frase[::-1]
if frase==frase2:
    print('a frase {} é um palindromo'.format(frase))
else:
    print('a frase {} não é um palindromo'.format(frase))
print(frase)
print(frase2)
