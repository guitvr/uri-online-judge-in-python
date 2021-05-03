while True:
    try:
        m, n = [int(i) for i in str(input()).split()]
    except:
        break
    else:
        if m <= 0 or n <= 0:
            break
        elif m > n:
            m, n = n, m
        
        soma = 0

        for i in range(m, n+1):
            print(i, end=' ')
            soma += i
        
        print(f'Sum={soma}')
