def identidade(m):
    for linha in range(ORDEM):
        for coluna in range (ORDEM):
            if linha==coluna:
                if m[linha][coluna]!=1:
                    return False
            elif m[linha][coluna]!=0:
                return False
    return True
    
ORDEM=3   
m=[[None]*ORDEM for i in range(ORDEM)]
for linha in range(ORDEM):
    for coluna in range (ORDEM):
        m[linha][coluna]=int(input('input'))
print(f'{identidade(m)}')
