#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primterm=int(input('digite o 1° da pa'))
razao=int(input('digite a razão da pa'))
print(primterm)
for c in range(1,10):
    calculo= primterm+(razao*c)
    print(calculo)
