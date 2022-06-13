#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
lista=[]
for c in range(1, 6):
    lista.append(input('digite seu peso'))
print(max(lista))
print(min(lista))
