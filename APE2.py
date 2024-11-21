aulas=int(input('Quantidades de aulas: '))
faltas=int(input('Total de aula assistida: '))
f=((aulas-faltas)/aulas)*100
print(f'A frenquêcia do aluno é de {f}%')