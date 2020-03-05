import random

ListOfWords = ['rajtuzy',
               'pasztet',
               'golonka',
               'kaszanka',
               'kiełbasa',
               'kibel',
               'ubikacja',
               'kuropatwa',
               'stójka',
               'gruczoł',
               'torbiel',
               'drzazga',
               'konkubinat',
               'konglomeracja',
               'kopyto',
               'machlojki']

RandomWord = random.choice(ListOfWords)

ShuffledWord = ','.join(RandomWord)
ShuffledWord = ShuffledWord.split(',')
random.shuffle(ShuffledWord)
print('Zgadnij na jakie słowo składają się wyświetlane litery')
print('Aby się poddać wprowadź Q lub q')

for i in range(len(ShuffledWord)):
    print(ShuffledWord[i], end='')
print()

while 1:
    Guess = input()
    if Guess == RandomWord or Guess == 'Q' or Guess == 'q':
        break

if Guess == RandomWord:
    print('Brawo zgadłeś')
