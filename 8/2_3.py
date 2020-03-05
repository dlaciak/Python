import random

RandomNumber = random.randint(1,30)
print(RandomNumber)

print('Wylosowałem liczbę z zakresu 1-30. Odganij ją\n')

while 1:
    Guess = int(input())
    if Guess == RandomNumber:
        break
print('Brawo wygrałeś!')
