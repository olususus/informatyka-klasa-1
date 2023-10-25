import random

AAA = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

srednia_harmoniczna = len(AAA) / sum(1 / x for x in AAA)

tablica_nieparzyste = [x for x in AAA if x % 2 != 0]
print("Liczby nieparzyste:", " ".join(map(str, tablica_nieparzyste)))

n = 10
losowe_wartosci = random.sample(range(n), 3)
losowe_wartosci.sort()

if losowe_wartosci[0] == 0 and losowe_wartosci[2] == n:
    print("Podział został dokonany poprawnie.")
else:
    print("Podział nie został dokonany poprawnie.")

element = 10
indeksy_elementu = [i for i, x in enumerate(AAA) if x == element]
print("Indeksy elementu", element, "to:", indeksy_elementu)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

liczby_pierwsze = sum(1 for num in AAA if is_prime(num))
print("Liczba liczb pierwszych w tablicy: ", liczby_pierwsze)
