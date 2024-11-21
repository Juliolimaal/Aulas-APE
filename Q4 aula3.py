while True:
    nota1=float(input('Digite sua primeira nota: '))
    if nota1 <0 or nota1 >10:
        print('Nota invalida')
    else:
        break
while True:
    nota2=float(input('Digite sua segunda nota: '))
    if nota2<0 or nota2>10:
        print('Nota invalida')
    else:
        break
soma=(nota1+nota2)/2
print(f'Media = {soma:.2f}')