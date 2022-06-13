num= int(input('digite um numero inteiro'))
escolha= int(input('escolha: \n 1 para binario \n 2 para octal \n 3 para exadecimal'))
if escolha==1:
    print(' o numero {} em binario é {}'.format(num, bin(num)))
elif escolha==2:
    print('o numero {} em octal é {}'.format(num, oct(num)))
elif escolha==3:
    print('o numero {} em exadecimal é {}'.format(num, hex(num)))