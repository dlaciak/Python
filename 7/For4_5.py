'''4. Napisz prosty program, który wykona się zadaną przez użytkownika liczbę razy.
Z każdym uruchomieniem pętli wyświetli informacje:
– czy liczba jest wielokrotnością 3
– czy liczba jest wielkorotnością 4
– wyświtli „hurra” jeżeli liczba dzieli się zarówno przez 3 jak i 4
– wyświetli gwiazdkę, jeśli żaden z powyższych warunków nie jest spełniony

5. Spróbuj wyświetlić choinkę z trójkątów w taki sposób,
aby każdy poziom choinki był o 1 wiersz dłuższy:'''


# -----------------------------------------------------------------------

HowMuch = int(input('Ile razy wykonać program?\n'))

for i in range(HowMuch):
    DivideBy3 = False
    DivideBy4 = False
    Number = int(input('Podaj liczbę naturalną.\n'))
    if Number % 3 == 0:
        DivideBy3 = True
    if Number % 4 == 0:
        DivideBy4 = True
    if DivideBy3 and DivideBy4:
        print('Podzielne przez 3 i 4')
    elif DivideBy3:
        print('Podzielne przez 3')
    elif DivideBy4:
        print('Podzielne przez 4')
    else:
        print('*')


#------------------------

Levels = int(input('Ile poziomów ma mieć choinka?\n'))

for k in range(Levels):
    print('*')
    print('**')
    if k >= 1:
        for j in range(k):
            print('*'*(3+j))


