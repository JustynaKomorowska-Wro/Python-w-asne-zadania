print('podaj liczbę')
liczba = int(input())
fib1 = 0
fib2 = 1
licznik = 3
while licznik <= liczba:
    suma = fib1 + fib2
    fib1 = fib2
    fib2 = suma
    licznik = licznik + 1
print(str(fib2) + ' jest ' + str(liczba) + ' w ciągu Fibbonaciego.')

