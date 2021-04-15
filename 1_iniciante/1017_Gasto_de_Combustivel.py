tempo = int(input())
vel = int(input())
consumo = 12

distancia = vel * tempo
combustivel = distancia / consumo

print(f'{combustivel:.3f}')
