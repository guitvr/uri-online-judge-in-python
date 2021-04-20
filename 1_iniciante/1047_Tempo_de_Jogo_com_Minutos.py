hora_i, minuto_i, hora_f, minuto_f = [int(i) for i in str(input()).split()]

minuto_i = (hora_i * 60) + minuto_i
minuto_f = (hora_f * 60) + minuto_f

if minuto_i == minuto_f:
    duracao = (24 * 60)
elif minuto_i > minuto_f:
    duracao = (24 * 60) - minuto_i + minuto_f
elif minuto_f > minuto_i:
    duracao = minuto_f - minuto_i

print(f'O JOGO DUROU {duracao//60} HORA(S) E {duracao%60} MINUTO(S)')
