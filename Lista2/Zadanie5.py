import random

colors = ["Karo", "Kier", "Pik", "Trefl"]

symbols = ["As", "Krol", "Krolowa", "Walet", "10", "9"]

list_of_cards = []

for i in colors:
    for j in symbols:
        list_of_cards.append((i, j))

print(f"Karty {list_of_cards}")
random.shuffle(list_of_cards)

random_cards = random.sample(list_of_cards, 10)
gracz_1 = random_cards[:5]
gracz_2 = random_cards[5:]

print(f"Gracz1 {gracz_1}")
print(f"Gracz2 {gracz_2}")

empty = []
power = {
    "As": 14,
    "Krol": 13,
    "Krolowa": 12,
    "Walet": 11,
    "10": 10,
    "9": 9
}

list_of_cards.sort()

while gracz_1 and gracz_2:
    card1 = gracz_1.pop(0)
    card2 = gracz_2.pop(0)

    if power[card1[1]] == power[card2[1]]:
        gracz_1.append(card1)
        gracz_2.append(card2)
    elif power[card1[1]] < power[card2[1]]:
        gracz_2.append(card1)
        gracz_2.append(card2)
    elif power[card1[1]] > power[card2[1]]:
        gracz_1.append(card1)
        gracz_1.append(card2)

if not gracz_2:
    print("Gracz1 wygral")
if not gracz_1:
    print("Gracz2 wygral")
