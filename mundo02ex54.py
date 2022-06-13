from datetime import date
ano_atual= date.today().year
tot_maior=0
tot_menor=0
for c in range (1,8):
    ano_nasc= int(input('digite em que ano voce nasceu'))
    if (ano_atual-ano_nasc)>=18:
        tot_maior+=1
    else:
        tot_menor+=1
print('possuem {} pessoas com maioridade'.format(tot_maior))
print('possuem {} de menor'.format(tot_menor))