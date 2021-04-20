subfilo = input()
classe = input()
ordem = input()

animais = {
    'aguia': ('vertebrado', 'ave', 'carnivoro'),
    'pomba': ('vertebrado', 'ave', 'onivoro'),
    'homem': ('vertebrado', 'mamifero', 'onivoro'),
    'vaca': ('vertebrado', 'mamifero', 'herbivoro'),
    'pulga': ('invertebrado', 'inseto', 'hematofago'),
    'lagarta': ('invertebrado', 'inseto', 'herbivoro'),
    'sanguessuga': ('invertebrado', 'anelideo', 'hematofago'),
    'minhoca': ('invertebrado', 'anelideo', 'onivoro')
}

for animal, caracteristicas in animais.items():
    if caracteristicas == (subfilo, classe, ordem):
        print(animal)
