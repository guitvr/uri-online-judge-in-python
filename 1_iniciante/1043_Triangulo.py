a, b, c = [float(i) for i in str(input()).split()]
if a + b > c and a + c > b and b + c > a:
    print(f'Perimetro = {a + b + c :.1f}')
else:
    print(f'Area = {((a + b) * c) / 2 :.1f}')
