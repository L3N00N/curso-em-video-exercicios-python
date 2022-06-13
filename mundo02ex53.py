frase= str(input('digite uma frase').upper().replace(' ', ''))
frase2= frase[::-1]
if frase==frase2:
    print('a frase {} é um palindromo'.format(frase))
else:
    print('a frase {} não é um palindromo'.format(frase))
print(frase)
print(frase2)