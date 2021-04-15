valores = str(input()).split()
a, b, c = int(valores[0]), int(valores[1]), int(valores[2])

MaiorAB = (a + b + abs(a-b)) // 2
MaiorABC = (MaiorAB + c + abs(MaiorAB - c)) // 2

print(f'{MaiorABC} eh o maior')
