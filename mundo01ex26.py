#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase= str(input('digite uma frase')).upper().strip()
print(frase.upper().count('a'))
print(frase.upper().find('a')+1)
print(frase.upper().rfind('a')+1)
