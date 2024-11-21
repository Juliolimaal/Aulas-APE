
while True:
    x=int(input('Diga a primeira coordenada: '))
    y=int(input('Diga a segunda coordenada: '))
    if x>0 and y>0:
        print('Primeiro')
    elif x<0 and y>0:
        print('Segundo')
    elif x<0 and y<0:
        print('Terceiro')
    elif y<0 and x>0:
        print('Quarto')
        break