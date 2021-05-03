while True:
    try:
        x, y = [int(i) for i in str(input()).split()]
        if 0 in (x, y):
            break
        elif x > 0 and y > 0:
            print('primeiro')
        elif x < 0 and y > 0:
            print('segundo')
        elif x < 0 and y < 0:
            print('terceiro')
        elif x > 0 and y < 0:
            print('quarto')    
    except:
        break
