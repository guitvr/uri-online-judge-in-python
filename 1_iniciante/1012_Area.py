v = str(input()).split()
a, b, c = float(v[0]), float(v[1]), float(v[2])

triangulo = a * c / 2
circulo = 3.14159 * c ** 2
trapezio = (a + b) * c / 2
quadrado = b ** 2
retangulo = a * b

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')
