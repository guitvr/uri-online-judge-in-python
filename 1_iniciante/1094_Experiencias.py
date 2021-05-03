n = int(input())
total = 0
cobaias = {'C': ['coelhos', 0], 'R': ['ratos', 0], 'S': ['sapos', 0]}

for i in range(n):
    teste = str(input()).split()
    quantia, tipo = int(teste[0]), teste[1]
    cobaias[tipo][1] += quantia
    total += quantia

print(f'Total: {total} cobaias')

for c in cobaias.values():
    print(f'Total de {c[0]}: {c[1]}')

for c in cobaias.values():
    print(f'Percentual de {c[0]}: {(c[1]/total)*100:.2f} %')
