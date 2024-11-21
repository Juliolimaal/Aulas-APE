alunos_aprovados=int(input('Qual a quantidade de alunos aprovados? '))

alunos_reprovados=int(input('Qual a quantidade de aluno reprovados? '))

soma = alunos_aprovados+alunos_reprovados

porcento = (alunos_aprovados/soma)*100

print(f'A porcentagem de alunos aprovados são de {porcento:.2f}%')