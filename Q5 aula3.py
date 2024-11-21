alcool = gasolina = diesel = 0

MENU = '''Escolha:
1 - Alcool
2 - Gasolina
3 - Diesel
4 - Sair
Opção; '''

while True:
    tipo_combustivel = int(input(MENU))
    if tipo_combustivel==4:
        break
    elif tipo_combustivel==1:
        alcool+=1
    elif tipo_combustivel==2:
        gasolina+=1
    elif tipo_combustivel==3:
        diesel+=1
    else:
        print('Opção inválida!')

print(f'alcool = {alcool}\nGasolina = {gasolina}\nDiesel = {diesel}')