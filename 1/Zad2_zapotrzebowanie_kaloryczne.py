#Zapotrzebowanie kaloryczne Python#1 FlyNerd

WagaKobiety = 63
WiekKobiety = 25
WzrostKobiety = 170
AktywnoscKobiety = 1.6
WspS_Kobiety = -161
WspS_Mezczyzni = 5

Aktywnosc = 0
TwojaWaga = float(input("Podaj swoją wagę ciała w kg\n"))
TwojWiek = int(input("Podaj swój wiek\n"))
TwojWzrost = int(input("Podaj swój wzrost w cm\n"))
CzyMezczyzna = input("Jesteś kobietą czy mężczyzną? K/M\n")

print("\nWybierz rodzaj swojej aktywności fizycznej")
print("#1 Praca siedząca, brak dodatkowej aktywności fizycznej")
print("#2 Praca niefizyczna, mało aktywny tryb życia")
print("#3 Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu")
print("#4 Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu")
print("#5 Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu")
RodzajAktywnosci = int(input("Wprowadz cyfrę od 1 do 5\n"))

if RodzajAktywnosci == 1:
    Aktywnosc = 1.2
elif RodzajAktywnosci == 2:
    Aktywnosc = 1.4
elif RodzajAktywnosci == 3:
    Aktywnosc = 1.6
elif RodzajAktywnosci == 4:
    Aktywnosc = 1.8
elif RodzajAktywnosci == 5:
    Aktywnosc = 2.0
else:
    print("Wprowadzono nieprawidłową wartość")

ZapotrzebonieKobiety = (10 * WagaKobiety + 6.25 * WzrostKobiety - 5 * WiekKobiety + WspS_Kobiety) * AktywnoscKobiety
print("Zapotrzebowanie kaloryczne przykładowej kobiety wynosi: {} kcal" .format(ZapotrzebonieKobiety))


if Aktywnosc >0 and Aktywnosc <=5:
    if CzyMezczyzna == "K" or CzyMezczyzna == 'k':
        TwojeZapotrzebowanie = (10 * TwojaWaga + 6.25 * TwojWzrost - 5 * TwojWiek + WspS_Kobiety) * Aktywnosc
        print("Kobietko, Twoje zapotrzebowanie kaloryczne wynosi: {:.2f} kcal" .format(TwojeZapotrzebowanie))
    elif CzyMezczyzna == "M" or CzyMezczyzna == 'm':
        TwojeZapotrzebowanie = (10 * TwojaWaga + 6.25 * TwojWzrost - 5 * TwojWiek + WspS_Mezczyzni) * Aktywnosc
        print("Byku, Twoje zapotrzebowanie kaloryczne wynosi: {:.2f} kcal" .format(TwojeZapotrzebowanie))
    else:
        print("Błędnie wprowadzona płeć")




