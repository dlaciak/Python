''' Do zmiennej sentence przypisz zdanie, a następnie:

    Policz wszystkie znaki w napisie
    Nie modyfikując zmiennej sentence wyświetl słowo „prosty”
    Wyświetl znak o indeksie (czy za każdym razem rozumiesz co się dzieje?):
        7
        12
        -4
        37
    Wprowadź do zdania 2 błędy ortograficzne'''

sentence = 'Aurel to śmietnik i margines społeczny'
print('Ilośc znaków w tekście to {}' .format(len(sentence)))
print(sentence[9:18])
print('7. znak to: {}' .format(sentence[7]))
print('12. znak to: {}' .format(sentence[12]))
print('-4. znak to: {}' .format(sentence[-4]))
print('37. znak to: {}' .format(sentence[37]))
sentence = sentence[0] + 'ó' + sentence[2:27] + 'z' + sentence[28:len(sentence)]
print(sentence)
