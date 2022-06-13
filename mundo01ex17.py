#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
num1= float(input('digite o comprimento do cateto oposto'))
num2= float(input('digite o comprimento do cateto adjacente'))
hip= hypot(num1, num2)
print(hip)
