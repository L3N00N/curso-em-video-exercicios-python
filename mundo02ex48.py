soma=0
cont=0
for c in range(3,501,3):
    if c%3==0 and c%2>0:
        soma+= c
        cont+=1
        print(c)
print(soma)
print(cont)