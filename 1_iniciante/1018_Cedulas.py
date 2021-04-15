valor = int(input())

print(valor)

for nota in (100, 50, 20, 10, 5, 2, 1):
    qnt = valor // nota
    valor = valor % nota
    print(f'{qnt} nota(s) de R$ {nota},00')
