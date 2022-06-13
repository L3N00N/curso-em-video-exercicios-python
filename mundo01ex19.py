from random import shuffle
alun1= str(input('digite o 1º nome'))
alun2= str(input('digite o 2º nome'))
alun3= str(input('digite o 3º nome'))
alun4= str(input('digite o 4º nome'))
lista= [alun1, alun2, alun3, alun4]
ordem= shuffle(lista)
print('o aluno sorteado foi {}'.format(ordem))