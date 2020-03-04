#Kalkulator BMI

'''Program powinien sprawdzić czy BMI należy do jednego z 4 wyników:
 niedowaga/waga normalna/lekka nadwaga i nadwaga.
 Ponadto w przypadku nadwagi chcemy sprawdzić czy mamy doczynienia z otyłością. '''

Wzrost = float(input("Podaj swój wzrost w metrach\n"))
Waga = float(input("Podaj swoją wagę w kg\n"))
BMI = Waga/Wzrost ** 2
print("Twoje BMI wynosi {:.2f}" .format(BMI))

if BMI < 18.5:
    print('Masz Niedowagę')
elif 18.5 <= BMI < 24:
    print('Twoja waga jest w normie')
elif 24 <= BMI < 26.5:
    print('Masz lekką nadwagę')
else:
    print('Masz nadwage')
    if 30 < BMI < 35:
        print('Dodatkowo stwierdzam otyłość I stopnia')
    elif 35 <= BMI < 40:
        print('Dodatkowo stwierdzam otyłość II stopnia')
    elif BMI >=40:
        print('Dodatkowo stwierdzam otyłość III stopnia')
   
