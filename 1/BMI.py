#Kalkulator BMI

print('Spiewajace fortepiany')

Wzrost = float(input("Podaj swój wzrost w metrach\n"))
Waga = float(input("Podaj swoją wagę w kg\n"))
BMI = Waga/Wzrost ** 2
print("Twoje BMI wynosi {:.2f}" .format(BMI))
