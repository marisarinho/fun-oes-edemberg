def somar(v):
    soma=0
    for i in v:
        soma+=i
    return soma
    
v=[6,3,8,7,2,5]    
print(f'{somar(v)}')

#versao inserindo valores 

def somar(v):
    soma=0
    for i in v:
        soma+=i
    return soma
    
v=list(map(int,input().split()))
print(f'{somar(v)}')



def somar(v):
    soma=0
    for i in v:
        soma+=i
    return soma
tam=int(input('tamanho vtor'))
v=[None]*tam
for i in range(tam):
    v[i]=int(input(' valores'))
print(f'{somar(v)}')
