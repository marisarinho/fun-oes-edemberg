def media(n1,n2,n3):
    media=((n1+n2+n3)/3)
    return media
def conceito(n1,n2,n3):
    a=media(n1,n2,n3)
    aluno=''
    if a>8:
        aluno='A'
    elif a>=5 and a<=8:
        aluno='B'
    elif a<5:
        aluno='C'
    return aluno

n1,n2,n3=map(int,input().split())
print(media(n1,n2,n3))
print(conceito(n1,n2,n3))
