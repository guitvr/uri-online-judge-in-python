peca1, qnt1, valor1 = str(input()).split()
peca2, qnt2, valor2 = str(input()).split()

total = int(qnt1) * float(valor1) + int(qnt2) * float(valor2)

print(f'VALOR A PAGAR: R$ {total:.2f}')
