def fatorial(num1):
    fat=1
    for i in range(2,num1+1):
        
        fat*=i
    return fat
num1=int(input('numero'))
print(f'{fatorial(num1)}')
