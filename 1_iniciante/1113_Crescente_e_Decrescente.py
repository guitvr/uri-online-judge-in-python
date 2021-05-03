while True:
    try:
        x, y = [int(i) for i in str(input()).split()]
    except:
        break
    else:
        if x == y:
            break
        elif x > y:
            print('Decrescente')
        elif x < y:
            print('Crescente')
