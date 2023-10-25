import math
import time
print('Kalkulator v2')
def PKWadratu(r):
    return r*r
def prownoleglo(a,h):
    return a*h
def pprosto(a,b):
    return a*b
def ptrapez(a,b,h):
    return a+b*h/2
def ptroj(a,h):
    return (a*h)/2
def pkola(r):
    return math.pi *r**2

print('Wybierz co chcesz obliczyć:')
print('Pola: kwadrat, rownoleglobok, prostokata, trapez, kolo')

while True:
    inp = input()
    if inp == "kwadrat":
        uno = float(input())
        print(PKWadratu(uno))
    elif inp == "rownoleglobok":
        uno1 = float(input())
        uno12 = float(input())
        print(prownoleglo(uno1, uno12))
    elif inp == "prostokata":
        uno2 = float(input())
        uno21 = float(input())
        print(pprosto(uno2, uno21))
    elif inp == "trapez":
        uno3 = float(input())
        uno31 = float(input())
        uno32 = float(input())
        print(ptroj(uno3, uno31, uno32))
    elif inp == "kolo":
        data = float(input())
        print(pkola(data))
    else:
        break