#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num= int(input('digite um numero entre 0 e 9999'))
unid= num//1 % 10
print(unid)
dez= num//10 % 10
print(dez)
cent= num//100 % 10
print(cent)
milh= num// 1000 % 10
print(milh)
