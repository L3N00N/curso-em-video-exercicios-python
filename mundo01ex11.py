Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados. 
larg= float(input('Digite a largura da parede em metros'))
h= float(input('digite a altura da parede em metros'))
m2_parede= (larg*h)
print('a parede possui {} mtros quadr e sera necessaria {} litros de tinta'.format(m2_parede, (m2_parede/2)))
