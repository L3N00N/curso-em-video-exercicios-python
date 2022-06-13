soma=0
for c in range(1, 7):
    num=int(input('digite o {} numero'.format(c)))
    if num%2==0:
        soma+=num
print(soma)