'''
Utwórz nowy plik np. jednostki.py, który po podaniu przez użytkownika długości w cm będzie wyświetlał wynik w metrach i calach zaokrąglając do 4 miejsc po przecinku.
Podobny skrypt możesz wykonać dla zamiany kg na funty.
Wynik wyświetl używając dowolnego sposobu formatowania tekstu.
'''

dlugosc_cm = float(input('Wprowadź wartość w cm\n'))
dlugosc_m = dlugosc_cm/100
dlugosc_cale = dlugosc_cm * 0.39370
print('{:.2f} cm to {:.2f} metra' .format (dlugosc_cm, dlugosc_m))
print('{:.2f} cm to {:.2f} cala' .format (dlugosc_cm, dlugosc_cale))


'''
Napisz skrypt, który, który obliczy stan konta za kilka lat. Program pyta użytkownika o:

    stan początkowy konta,
    stopę oprocentowania rocznego (zwróć uwagę, że odsetki podlegają miesięcznej kapitalizacji)
    liczbę lat na lokacie.

Wynik wyświetl jako zdanie używając dowolnego sposobu formatowania tekstu.
Wypisz np. takie zdanie:
Twoje *stan_początkowy* zł przez *czas* lata na lokacie *oprocentowanie* % urośnie do *wynik*.
'''

StanPoczatkowy = float(input('Wprowadź stan początkowy konta\n'))
StopaRoczna = float(input('Wprowadź wartość rocznej stopy oprocentowania\n'))
LiczbaLat = float(input('Wprowadź liczbę lat na lokacie\n'))
LiczbaMiesiecy = LiczbaLat*12

WartoscOczekiwana = StanPoczatkowy * ((1 + StopaRoczna/(100*12)) ** LiczbaMiesiecy)

print('Stan początkowy równy {} po {:.0f} miesiącach na oprocentowaniu {}% urośnie do {:.2f} złotych' .format(StanPoczatkowy,LiczbaMiesiecy,StopaRoczna,WartoscOczekiwana))
