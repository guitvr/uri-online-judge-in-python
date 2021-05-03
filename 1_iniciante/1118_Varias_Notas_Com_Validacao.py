while True:
    soma = 0
    
    for i in range(2):
        while True:
            nota = float(input())
            if 0 <= nota <= 10:
                break
            print('nota invalida')
        soma += nota 

    media = soma / 2
    print(f'media = {media:.2f}')

    while True:
        print('novo calculo (1-sim 2-nao)')
        x = int(input())
        if x in (1, 2):
            break

    if x == 2:
        break
