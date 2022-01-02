entrada = [int(i) for i in input().split()]
A = entrada[0]

for i in entrada[1:]:
    if i > 0:
        N = i
        break

soma = 0
for i in range(N):
    soma += A + i

print(soma)
