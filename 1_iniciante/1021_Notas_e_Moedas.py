valor = float(input())

print('NOTAS:')
for nota in (100, 50, 20, 10, 5, 2):
    qnt = valor // nota
    valor = valor % nota
    print(f'{qnt:.0f} nota(s) de R$ {nota}.00')
print('MOEDAS:')
for moeda in (1, 0.50, 0.25, 0.10, 0.05, 0.01):
    qnt = int(valor*100) // int(moeda*100)
    valor = (int(valor*100) % int(moeda*100)) / 100
    print(f'{qnt:.0f} moeda(s) de R$ {moeda:.2f}')
