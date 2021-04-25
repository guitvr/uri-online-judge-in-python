renda = float(input())

IR = ((4500, 0.28), (3000, 0.18), (2000, 0.08))

if renda <= 2000:
    print('Isento')
else:
    imposto = 0
    for faixa, taxa in IR:
        if renda > faixa:
            imposto += (renda - faixa) * taxa
            renda -= renda - faixa
    print(f'R$ {imposto:.2f}')
