grenais = 0
inter = 0
gremio = 0
empates = 0

while True:
    i, g = [int(i) for i in input().split()]
    grenais += 1
    if i > g:
        inter += 1
    elif g > i:
        gremio += 1
    else:
        empates += 1
    
    print('Novo grenal (1-sim 2-nao)')

    r = int(input())

    if r == 2:
        break

if inter > gremio:
    vencedor = 'Inter venceu mais'
elif gremio > inter:
    vencedor = 'Gremio venceu mais'
else:
    vencedor = 'Nao houve vencedor'

print(f'{grenais} grenais')
print(f'Inter:{inter}')
print(f'Gremio:{gremio}')
print(f'Empates:{empates}')
print(vencedor)
