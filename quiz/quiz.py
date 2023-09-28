print('Witaj w quizie')
answer=input('Czy jesteś gotowy  (tak/nie) :')
wynik=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Pytanie 1: Jaki jest twój ulubiony język programowania?')
    if answer.lower()=='python':
        wynik += 1
        print('dobrze')
    else:
        print('źle :(')
 
 
    answer=input('Pytanie 2: Czy mnie lubisz ')
    if answer.lower()=='tak':
        wynik += 1
        print('dobrze')
    else:
        print('Źle :(')
 
    answer=input('Pytanie 3: masz githuba?')
    if answer.lower()=='tak':
        wynik += 1
        print('dobrze')
    else:
        print('źle :(')
 
print('Dziękuje za branie udziału w moim quizie. odpowiedziałeś na',wynik,"pytań poprawnie")
mark=(wynik/total_questions)*100
print('Punkty:',mark)
print('Papatki')