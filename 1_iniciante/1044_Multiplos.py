a, b = [int(i) for i in str(input()).split()]

if a % b == 0 or b % a == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
