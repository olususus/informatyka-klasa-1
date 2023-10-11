import random

# 1. Wygenerowanie tablicy zawierającej n losowych elementów z zakresem min i max
n = 10  # liczba elementów w tablicy
min_val = 1  # minimalna wartość
max_val = 20  # maksymalna wartość

tablica = [random.randint(min_val, max_val) for _ in range(n)]
print(tablica)

# 2. Znalezienie maksymalnej i minimalnej wartości w tablicy
max_value = tablica[0]
min_value = tablica[0]

for element in tablica:
    if element > max_value:
        max_value = element
    if element < min_value:
        min_value = element

print(f'Max: {max_value}, Min: {min_value}')

# 3. Znalezienie liczby wystąpień danego elementu w tablicy
element = 1  # przykład: liczba 1
count = tablica.count(element)
print(f'Liczba wystąpień {element}: {count}')

# 4. Sprawdzenie, ile liczb pierwszych zawiera tablica
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_count = sum(1 for num in tablica if is_prime(num))
print(f'Liczba liczb pierwszych w tablicy: {prime_count}')

# 5. Przepisanie elementów mniejszych od n do drugiej tablicy i wyświetlenie jej
n = 5  # przykład: n = 5
tablica2 = [x for x in tablica if x < n]
print(tablica2)

# 6. Przyjęcie n liczb od użytkownika, zapisanie liczb parzystych w nowej liście
n = 5  # przykład: n = 5
liczby_parzyste = []

for i in range(n):
    liczba = int(input(f'Podaj liczbę {i + 1}: '))
    if liczba % 2 == 0:
        liczby_parzyste.append(liczba)

print(f'Liczby parzyste: {liczby_parzyste}')
