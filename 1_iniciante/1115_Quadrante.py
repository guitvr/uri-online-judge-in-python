x = int(input())
y = int(input())

if x > y:
    x, y = y, x

for i in range(x+1, y):
    if i % 5 in (2, 3):
        print(i)
