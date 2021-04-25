num_positivos = []

for i in range(6):
    n = float(input())
    if n > 0:
        num_positivos.append(n)

qnt = len(num_positivos)
media = sum(num_positivos) / qnt

print(f'{qnt} valores positivos')
print(f'{media:.1f}')
