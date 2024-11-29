import random

lista = []
for i in range (3):
    a = input("Podaj fakt o sobie:")
    lista.append(a)
print("Twój losowy fakt to",random.choice(lista))
