print('Sprawdzę dla Ciebie, czy dane słowo jest palindromem. Podaj słowo:')
slowo = input()
odwrocone = slowo[::-1]
if slowo.lower() == odwrocone.lower():
    print('Słowo jest palindromem, ponieważ ' + slowo.lower() + ' po odwróceniu to ' + odwrocone.lower() + '.')
else:
    print('Słowo nie jest palindromem, ponieważ ' + slowo.lower() + ' po odwróceniu to ' + odwrocone.lower() + '.')
