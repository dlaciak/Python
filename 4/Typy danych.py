'''
Utwórz i wyświetl dowolne zmienne przechowujące wartości wg. typów:
Liczby (Numbers) – całkowite/zmiennoprzecinkowe
Teksty (String)
Typ logiczny (Bool)
Listy (List)
Krotki (Tuple)
Słowniki (Dictionary)
'''

'Liczby'

LiczbaCalkowita = 3
LiczbaRzeczywista = 3.01

'Tekst'

Tekst = 'Aurel to śmietnik'

'Typ logiczny'

AlwaysTrue = True
AlwaysFalse = False

print('Liczba całkowita ma wartość {}, a liczba rzeczywista {}' .format(LiczbaCalkowita,LiczbaRzeczywista))
print(Tekst)
print('AlwaysTrue to {}, AlwaysFalse to {}' .format(AlwaysTrue,AlwaysFalse))
print('Typy wymienionych zmiennych to kolejno: {}, {}, {}, {}, {}' .format(type(LiczbaCalkowita),type(LiczbaRzeczywista),type(Tekst),type(AlwaysTrue),type(AlwaysFalse)))


# ------------------------------------------------------------------------

print('\n\nListy')
Lista1 = [1,2.3,True,'Hulajnoga']
print(Lista1)
print('Na co komu hulajnoga, jak może mieć rower')
Lista1[3] = 'rower'
print(Lista1)
print('Typ powyższej listy to: {}' .format(type(Lista1)))

# ------------------------------------------------------------------------

print('\n\nKrotki')
Krotka1 = (0,3.3,False,'Hulajnoga')
print(Krotka1)
print('Tu nie będzie roweru :( Krotki są niemutowalne')
#Krotka1[3] = 'rower'   nie zadziała bo krotki są niemutowalne (niezmienne)
print('Typ powyższej krotki to: {}' .format(type(Krotka1)))

# ------------------------------------------------------------------------

print('\n\nSlowniki')
Slownik1 = {0 : 'zero', 'Aurel' : 'śmietnik', 'klucz' : 'wartość'}
print(Slownik1)
print('Typ powyższego slownika to: {}' .format(type(Slownik1)))
print('Dorzućmy jakiś pojazd')
Slownik1['Pojazd'] = 'Hulajnoga'
print(Slownik1)
print('Wartość klucza Aurel to: {}' .format(Slownik1['Aurel']))
print('Klucze w słowniku: {}' .format(Slownik1.keys()))
print('Wartości w słowniku: {}' .format(Slownik1.values()))
print('Na co komu hulajnoga, jak może mieć rower')
Slownik1['Pojazd'] = 'Rower'   #można zmieniać wartości przypisane do kluczy, ale klucze są już niemutowalne (chyba ...)
print(Slownik1)


