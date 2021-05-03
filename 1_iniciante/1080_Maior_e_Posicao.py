v = []

for i in range(100):
    n = int(input())
    v.append(n)

print(max(v))
print(v.index(max(v))+1)
