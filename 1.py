def menor(num1,num2,num3):
    menor=num1
    if num2< menor:
        menor=num2
    if num3<menor:
        menor=num3
    return menor
num1,num2,num3=map(int,input('numero').split())
print(f'{menor(num1,num2,num3)}')

