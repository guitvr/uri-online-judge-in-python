n = int(input())
c = 1
while c <= n*4:
    if c % 4 == 0:
            print('PUM')
    else:
        print(c, end=' ')
    c += 1
