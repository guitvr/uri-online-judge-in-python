n = int(input())

for i in range(n):
    soma = 0
    x, y = [int(i) for i in str(input()).split()]

    if x > y:
        x, y = y, x

    x += 1
    
    while x < y:
        if x % 2 != 0:
            soma += x
        x += 1

    print(soma)
