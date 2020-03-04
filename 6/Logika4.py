'''Utwórz zbiór imion męskich i żeńskich. Poproś użytkownika o podanie imienia.
Sprawdź czy imię jest męskie czy żeńskie i wyświetl na ten temat informację.
Jeżeli imienia nie ma na liście wyświetl komunikat „Nie znamy tego imienia.”
Następnie użytkownik poda informację czy imię jest męskie czy żeńskie. Dodaj imię do listy.
'''

#-------------------------------------------------------


Names = {'Ania' : 'Żeńskie',
         'Marta' : 'Żeńskie',
         'Aleksandra' : 'Żeńskie',
         'Patrycja' : 'Żeńskie',
         'Monika' : 'Żeńskie',
         'Dawid' : 'Męskie',
         'Aureliusz' : 'Męskie',
         'Krzysztof' : 'Męskie',
         'Dorian' : 'Męskie',
         'Maciek' : 'Męskie'
}

Name = input('Podaj imię\n')

if not Name in Names:
    print('Tego imienia nie ma w spisie. Dodamy je. To imię męskie czy żeńskie? M/Z?')
    Gender = input()
    if Gender == 'M' or Gender == 'm':
        Names[Name] = 'Męskie'
        print('Zaktualizowana lista:\n {}' .format(Names))
    elif Gender == 'Z' or Gender == 'z':
        Names[Name] = 'Żeńskie'
        print('Zaktualizowana lista:\n {}' .format(Names))
    else:
        print('Błąd')
        
else:
    print('Imię {} to imię {}.' .format(Name,Names[Name].lower()))

