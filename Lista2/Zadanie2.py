import random

countries = ['Uruguay', 'Russia', 'Saudi Arabia', 'Egypt', 'Spain', 'Portugal', 'Iran', 'Morocco', 'France', 'Denmark',
             'Peru', 'Australia', 'Croatia', 'Argentina', 'Nigeria', 'Iceland', 'Brazil', 'Switzerland', 'Serbia',
             'Costa Rica', 'Sweden', 'Mexico',

             'Korea Republic', 'Germany', 'Belgium', 'England', 'Tunisia', 'Panama', 'Colombia', 'Japan', 'Senegal',
             'Poland']

random.shuffle(countries)

A = [random.choice(countries)]
B = [random.choice(countries)]
C = [random.choice(countries)]
D = [random.choice(countries)]
E = [random.choice(countries)]
F = [random.choice(countries)]
G = [random.choice(countries)]
H = [random.choice(countries)]

print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
print(G)
print(H)
