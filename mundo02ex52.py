#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num=int(input('digite um numero'))
tot=0
for c in range(1,num+1):
    if num%c==0:
        print('\033[34m', end='')
        tot+=1
    else:
        print('\033[m', end='')
    print('{}'.format(c), end='')
print('O numero {} foi divisivel {} vezes'.format(num, tot))
