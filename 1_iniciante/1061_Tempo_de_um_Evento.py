d1 = int(str(input())[4:].strip())
hms1 = [int(i) for i in str(input()).split(' : ')]

d2 = int(str(input())[4:].strip())
hms2 = [int(i) for i in str(input()).split(' : ')]

m = 60
h = 60*m
d = 24*h

i = d1 * d + hms1[0]*h + hms1[1]*m + hms1[2]
f = d2 * d + hms2[0]*h + hms2[1]*m + hms2[2]

t = f - i

w = t // d
x = (t % d) // h
y = ((t % d) % h) // m
z = ((t % d) % h) % m

print(f'{w} dia(s)')
print(f'{x} hora(s)')
print(f'{y} minuto(s)')
print(f'{z} segundo(s)')
