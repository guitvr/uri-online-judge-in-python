inicio, fim = [int(i) for i in str(input()).split()]

if inicio == fim:
    duracao = 24
elif inicio > fim:
    duracao = 24 - inicio + fim
elif fim > inicio:
    duracao = fim - inicio

print(f'O JOGO DUROU {duracao} HORA(S)')
