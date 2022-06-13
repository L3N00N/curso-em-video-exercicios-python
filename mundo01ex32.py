#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
from datetime import date
ano= int(input('digite um ano, digitee 0 para analisar o ano atual'))
if ano==0:
    ano= date.today().year
if (ano%4)==0 and (ano%100)!=0 or (ano%400)==0:
    print('o ano {} não é bissexto'.format(ano))
else:
     print('o ano {} é bissexto'.format(ano))
