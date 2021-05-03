from decimal import Decimal
i, j = Decimal('0.0'), Decimal('1.0')
while i <= 2:
    for x in range(3):
        if int(i*10) % 10 == 0:
            print(f'I={int(i)} J={int(j+x)}')
        else:
            print(f'I={i} J={j+x}')
    i += Decimal('0.2')
    j += Decimal('0.2')
