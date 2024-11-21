duracao_em_min=int(input('Quantos minutos terá a avaliação? '))

duracao_avaliacao_seg= duracao_em_min * 60


aulas_necessarias = duracao_em_min / 50

print(f'A quantidade de segundos serão: {duracao_avaliacao_seg}')

print(f'A quantidade de aulas necessária para a avaliação será: {aulas_necessarias:.2f} aulas')