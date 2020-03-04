'''Utwórz spis oglądanych seriali.
Każdy serial powinen mieć przypisaną ocenę w skali od 1-10.
Zapytaj użytkownika jaki serial chce obejrzeć.
W odpowiedzi podaj jego ocenę.
Zapytaj użytkownika o dodanie kolejnego serialu i oceny.
Dodaj serial do spisu.'''



Serials = {'Breaking bad' : 1, 'Game of Thrones' : 2, 'The Witcher' : 3, 'Rick and Morty' : 4}

print('Aktualna lista seriali w bazie to: {}' .format(list(Serials.keys())))
WybranySerial = input('Podaj nazwę aby zobaczyć ocenę\n')

if WybranySerial in Serials:
    print('Ocena serialu {} to {}' .format(WybranySerial, Serials[WybranySerial]))
else:
    print('Nie ma takiego serialu na liście')

NowySerial,NowaOcena = input('Wprowadź nowy serial\n'),float(input('Wprowadź jego ocenę\n'))
if NowySerial not in Serials:
    Serials[NowySerial] = NowaOcena
    print('Aktualna lista seriali w bazie to: {}' .format(list(Serials.keys())))
else:
    print('Serial, który chciałeś wprowadzić znajdował się już na liście')

