x = int(input())
y = int(input())

soma = 0

if x > y:
    x, y = y, x

if x % 2 != 0:
    x += 2
else:
    x += 1

for i in range(x, y):
    if i % 2 != 0:
        soma += i

print(soma)
