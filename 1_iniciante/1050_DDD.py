def get_cidade(ddd):
    ddd_cidade = {
        61: 'Brasilia',
        71: 'Salvador',
        11: 'Sao Paulo',
        21: 'Rio de Janeiro',
        32: 'Juiz de Fora',
        19: 'Campinas',
        27: 'Vitoria',
        31: 'Belo Horizonte'
    }
    return ddd_cidade.get(ddd, 'DDD nao cadastrado')


ddd = int(input())

print(get_cidade(ddd))
