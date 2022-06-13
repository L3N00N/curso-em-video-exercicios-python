#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
ang= float(input('digite um angulo'))
rad= radians(ang)
print('o angulo é {}, seu seno é {}, seu coseno {} e sua tangente {}'.format(ang, sin(rad), cos(rad), tan(rad)))
