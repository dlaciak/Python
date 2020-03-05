A = int(input('Podaj dowolną liczbę naturalną mniejszą od 15\n'))
Result = 1

while (A != 0):
    Result = Result * A
    A -= 1
print(Result)

A = int(input('Podaj dowolną liczbę naturalną mniejszą od 15\n'))    
Result = 1
for i in range (A):
    Result = Result * A
    A -= 1
print(Result)
    
