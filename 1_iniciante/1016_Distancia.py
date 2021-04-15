distancia = int(input())
vel_X = 60
vel_Y = 90

vel_rel = vel_Y - vel_X
tempo_min = int(distancia * 60 / vel_rel)

print(f'{tempo_min} minutos')
