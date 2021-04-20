v = [float(i) for i in str(input()).split()]
v.sort(reverse=True)

if v[0] >= v[1] + v[2]:
    print('NAO FORMA TRIANGULO')
elif v[0]**2 == v[1]**2 + v[2]**2:
    print('TRIANGULO RETANGULO')
elif v[0]**2 > v[1]**2 + v[2]**2:
    print('TRIANGULO OBTUSANGULO')
elif v[0]**2 < v[1]**2 + v[2]**2:
    print('TRIANGULO ACUTANGULO')

if v[0] == v[1] == v[2]:
    print('TRIANGULO EQUILATERO')
elif v[0] == v[1] or v[1] == v[2] or v[0] == v[2]:
    print('TRIANGULO ISOSCELES')
