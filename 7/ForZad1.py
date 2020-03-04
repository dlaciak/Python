#Suma kolejnych liczb naturalych w zależności ile ich jest

Sum = 0
for i in range(1,11):
    Sum = Sum + i
    print('{}. Suma w tym punkcie to {}' .format(i,Sum))

#sześcian pierwszych 10 liczb

Cube = 0
for i in range(1,11):
    print('Sześćian liczby {} jest równy {}' .format(i,i ** 3))

list = str(input('Podaj liste imion: '))
for i in list.split():
    print('hi ' + i)


