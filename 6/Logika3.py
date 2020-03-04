'''Trzy dowolne liczby zapisz do trzech zmiennych.
Znajdź największą liczbę.
Wyświetl liczby od największej do najmniejszej.'''

#-------------------------------------------------------

a = input('Wprowadź pierwszą liczbę\n')
b = input('Wprowadź drugą liczbę\n')
c = input('Wprowadź trzecią liczbę\n')

List = [a,b,c]
print('Wprowadzone liczby {}' .format(List))
print('Liczby posortowane od największej do najmniejszej:')
if a >= b and a >= c:
    if b >= c:
        print('{}, {}, {}' .format(a,b,c))
    else:
        print('{}, {}, {}' .format(a,c,b))
elif b >= c:
    if c >= a:
        print('{}, {}, {}' .format(b,c,a))
    else:
        print('{}, {}, {}' .format(b,a,c))
elif b >= a:
    print('{}, {}, {}' .format(c,b,a))
else:
    print('{}, {}, {}' .format(c,a,b))

