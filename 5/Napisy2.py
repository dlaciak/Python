'''Utwórz skrypt, który zapyta użytkownika o imię, nazwisko i numer telefonu, a następnie:

    Sprawdź czy imię i nazwisko składają się tylko z liter, a nr tel składa się wyłącznie z cyfr (wyświetl tę informację jako true/false)
    Użytkownicy bywają leniwi. Nie zawsze zapisują imię czy nazwisko z dużej litery – popraw ich
    Niektórzy podają numer telefonu z myślnikami lub z spacjami, usuń zbędne znaki z numeru
    Zakładając, że twoi użytkownicy noszą polskie imiona, sprawdź czy użytkownik jest kobietą
    Połącz dane w jeden ciąg personal za pomocą spacji
    Policz liczbę wszystkich znaków w napisie personal
    Podaj liczbę tylko liter w napisie personal

Podpowiedź – weź pod uwagę, że numery telefonów w Polsce są 9-cyfrowe'''

Name,Surname,PhoneNumber = input('Podaj swoję imię\n'),input('Podaj swoję nazwisko\n'),input('Podaj swój nr telefonu\n')

if Name.isalpha():
    print('Wpisane przez Ciebie imię składa się wyłącznie z liter')
else:
    print('Wpisane przez Ciebie imię nie składa się wyłącznie z liter')

if Surname.isalpha():
    print('Wpisane przez Ciebie imię składa się wyłącznie z liter')
else:
    print('Wpisane przez Ciebie imię nie składa się wyłącznie z liter')
    
if PhoneNumber.isdigit():
    print('Wpisane przez Ciebie imię składa się wyłącznie z cyfr')
else:
    print('Wpisane przez Ciebie imię nie składa się wyłącznie z cyfr')

#-----------------------------------------

if not Name.istitle():
    print ('Poprawiłem Twoje imię i nazwisko by zaczynało się z wielkiej litery: {} {}' .format(Name.capitalize(),Surname.capitalize()))

#-----------------------------------------

PhoneNumber = PhoneNumber.replace(' ','')
PhoneNumber = PhoneNumber.replace('-','')
print(PhoneNumber)

#-----------------------------------------    

if Name[len(Name)-1] == 'a' or Name[len(Name)-1] == 'A':
    print('Zakładam że jesteś kobietą')
else:
    print('Zakładam że jesteś mężczyzną')

# Można też tak imo nawet lepiej xD ale jak się nie zna to się kombinuję jak wyżej 

if Name.endswith('a'):
    print('Zakładam że jesteś kobietą')
else:
    print('Zakładam że jesteś mężczyzną')

    
#-----------------------------------------    

personal = Name + ' ' + Surname + ' ' + PhoneNumber
print(personal)

#-----------------------------------------

print('Liczba znaków w powyższym zapisie to: {}' .format(len(personal)))

#-----------------------------------------

CountOfLetters = len(personal) - personal.count(' ') - personal.count('1') - personal.count('2') - personal.count('3') - personal.count('4') - personal.count('5') - personal.count('6') - personal.count('7') - personal.count('8') - personal.count('9') - personal.count('0')
print('A liczba liter to {}' .format(CountOfLetters))

#można było założyć że nr tel składa się z 9 cyft i odjąć 9 po prostu no ale xD zliczmy sobie wystąpienia

