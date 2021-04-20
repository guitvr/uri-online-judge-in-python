cod, qnt = [int(i) for i in str(input()).split()]   # agora com List Comprehension  :)
lanches = {
    1: ('Cachorro Quente', 4.00), 
    2: ('X-Salada', 4.50),
    3: ('X-Bacon', 5.00),
    4: ('Torrada simples', 2.00),
    5: ('Refrigerante', 1.50)
    }
total = lanches[cod][1] * qnt
print(f'Total: R$ {total:.2f}')
