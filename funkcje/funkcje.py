def filtruj_slowa(lista_slow):
    wynik = [slowo for slowo in lista_slow if len(slowo) > 5]
    return wynik

def zamien_na_wielkie(tekst):
    return tekst.upper()

def druga_najmniejsza(lista_liczb):
    unikalne_liczby = list(set(lista_liczb))
    unikalne_liczby.sort()
    if len(unikalne_liczby) >= 2:
        return unikalne_liczby[1]
    else:
        return None

def licz_wystapienia(tekst, znak):
    return tekst.count(znak)

def suma_podzielnych_przez_3(lista_liczb):
    return sum([x for x in lista_liczb if x % 3 == 0])

def usun_duplikaty(lista):
    return list(set(lista))

from collections import Counter

def najczesciej_wystepujacy(lista_liczb):
    licznik = Counter(lista_liczb)
    najczestszy_element, ilosc_wystapien = licznik.most_common(1)[0]
    return najczestszy_element

def odwroc_liste(lista):
    return lista[::-1]

def polacz_i_posortuj(lista1, lista2):
    lista_wynikowa = lista1 + lista2
    lista_wynikowa.sort()
    return lista_wynikowa

def druga_najwieksza(lista_liczb):
    unikalne_liczby = list(set(lista_liczb))
    unikalne_liczby.sort(reverse=True)
    if len(unikalne_liczby) >= 2:
        return unikalne_liczby[1]
    else:
        return None

# Przykłady użycia funkcji:

# 10. Filtruj słowa dłuższe niż 5 znaków
lista_slow = ["kot", "pies", "samochod", "rower", "telewizor", "laptop"]
wynik = filtruj_slowa(lista_slow)
print(wynik)

# Pozostałe przykłady pozostają bez zmian.

# 11. Zamień na wielkie litery
tekst = "Hello, World!"
wynik = zamien_na_wielkie(tekst)
print(wynik)

# 12. Druga najmniejsza wartość
lista_liczb = [5, 2, 8, 1, 9, 2, 6]
wynik = druga_najmniejsza(lista_liczb)
print(wynik)

# 13. Licz wystąpienia znaku
tekst = "Hello, World!"
znak = "l"
wynik = licz_wystapienia(tekst, znak)
print(wynik)

# 14. Suma podzielnych przez 3
lista_liczb = [3, 6, 9, 12, 15, 18]
wynik = suma_podzielnych_przez_3(lista_liczb)
print(wynik)

# 15. Usuń duplikaty
lista = [1, 2, 2, 3, 4, 4, 5]
wynik = usun_duplikaty(lista)
print(wynik)

# 16. Najczęściej występujący element
lista_liczb = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
wynik = najczesciej_wystepujacy(lista_liczb)
print(wynik)

# 17. Odwróć listę
lista = [1, 2, 3, 4, 5]
wynik = odwroc_liste(lista)
print(wynik)

# 18. Połącz i posortuj listy
lista1 = [2, 4, 6]
lista2 = [1, 3, 5]
wynik = polacz_i_posortuj(lista1, lista2)
print(wynik)

# 19. Druga największa wartość
lista_liczb = [5, 2, 8, 1, 9, 2, 6]
wynik = druga_najwieksza(lista_liczb)
print(wynik)
