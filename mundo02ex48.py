#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma=0
cont=0
for c in range(3,501,3):
    if c%3==0 and c%2>0:
        soma+= c
        cont+=1
        print(c)
print(soma)
print(cont)
