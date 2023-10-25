import math


tablica_A = [1, 14, 21, 3, 42, 28, 7, 5, 35, 10]


tablica_podzielne_przez_7 = [x for x in tablica_A if x % 7 == 0]
tablica_reszta = [x for x in tablica_A if x % 7 != 0]


a = 7 
suma_podzielnych = sum(x for x in tablica_A if x % a == 0)


x = 7 
liczba_powtorzen = tablica_A.count(x)


min_value = min(tablica_A)
indeksy_minimalnych = [i for i, x in enumerate(tablica_A) if x == min_value]


srednia_harmoniczna = len(tablica_A) / sum(1 / x for x in tablica_A)


tablica_pierwiastek_calkowity = [x for x in tablica_A if math.sqrt(x).is_integer()]


print("Tablica podzielne przez 7:", tablica_podzielne_przez_7)
print("Suma liczb podzielnych przez", a, "to", suma_podzielnych)
print(x, "powtarza się", liczba_powtorzen, "razy w tablicy.")
print("Indeksy minimalnych wartości:", indeksy_minimalnych)
print("Średnia harmoniczna:", srednia_harmoniczna)
print("Liczby z pierwiastkiem całkowitym:", tablica_pierwiastek_calkowity)
