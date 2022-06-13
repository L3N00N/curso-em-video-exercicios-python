#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
prod= float(input('digite o valor do produto'))
prod2= prod-(prod*5/100)
print('o valor do produto é de {} R$ e com o desconto de 5% fica {}'.format(prod, prod2))
