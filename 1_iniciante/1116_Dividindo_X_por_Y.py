n = int(input())

for i in range(n):
    try:
        x, y = [int(i) for i in str(input()).split()]
        div = x / y
        print(f'{div:.1f}')
    except ZeroDivisionError:
        print('divisao impossivel')
        continue
    except:
        continue
