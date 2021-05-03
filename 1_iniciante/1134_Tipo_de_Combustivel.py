cod_prod = {1: ['Alcool', 0], 2: ['Gasolina', 0], 3: ['Diesel', 0]}  # {código: [produto, quantidade]}

while True:
    n = int(input())
    if n == 4:
        break
    elif n in cod_prod.keys():
        cod_prod[n][1] += 1

print('MUITO OBRIGADO')
for cod in cod_prod.keys():
    print(f'{cod_prod[cod][0]}: {cod_prod[cod][1]}')
