numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]  # Przykładowa lista liczb

# Wyświetlenie wszystkich liczb w odwrotnej kolejności
print("Liczby w odwrotnej kolejności:", numbers[::-1])

# Prośba o podanie liczby i sprawdzenie, czy znajduje się w liście
user_number = int(input("Podaj liczbę: "))
if user_number in numbers:
    print(f"Liczba {user_number} znajduje się w liście.")
else:
    print(f"Liczba {user_number} nie znajduje się w liście.")

# Wyświetlenie indeksu pierwszego wystąpienia danej liczby w liście
if user_number in numbers:
    index = numbers.index(user_number)
    print(f"Pierwsze wystąpienie liczby {user_number} ma indeks {index}.")

# Znalezienie ilości liczb większych niż 10 w liście
count_greater_than_10 = sum(1 for num in numbers if num > 10)
print(f"Ilość liczb większych niż 10 w liście: {count_greater_than_10}")
# Posortowanie listy w kolejności malejącej
sorted_numbers = sorted(numbers, reverse=True)
print("Posortowana lista malejąco:", sorted_numbers)

# Znalezienie drugiej największej liczby w liście
unique_numbers = list(set(numbers))
unique_numbers.sort()
second_largest = unique_numbers[-2]
print(f"Druga największa liczba w liście: {second_largest}")

# Stworzenie nowej listy zawierającej podwojoną wartość każdej liczby
doubled_numbers = [num * 2 for num in numbers]
print("Lista z podwojonymi liczbami:", doubled_numbers)

# Zliczenie ilości wystąpień danej liczby w liście
count_of_user_number = numbers.count(user_number)
print(f"Liczba wystąpień liczby {user_number} w liście: {count_of_user_number}")

# Wyświetlenie wszystkich liczb z ich indeksami
for index, num in enumerate(numbers):
    print(f"Indeks: {index}, Liczba: {num}")
