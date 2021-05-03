n = int(input())

for i in range(n):
    x, y, z = [float(i) for i in str(input()).split()]
    
    media_ponderada = (x*2 + y*3 + z*5) / 10

    print(f'{media_ponderada:.1f}')
