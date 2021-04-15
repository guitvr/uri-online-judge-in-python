p1 = str(input()).split()
p2 = str(input()).split()

x1, y1 = float(p1[0]), float(p1[1])
x2, y2 = float(p2[0]), float(p2[1])

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

print(f'{distancia:.4f}')
