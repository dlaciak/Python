'''
Trójkąt pitagorejski, to trójkąt prostokątny, którego boki są wyrażone liczbami naturalnymi a, b, c związanymi warunkiem: a2+b2=c2.

a) Poproś użytkownika o podanie długości boków A, B i C i sprawdź czy w ogóle możliwe jest utworzenie z nich trójkąta 

b) Odpowiedz czy trójkąt jest trójkątem pitagorejskim.

c) Szczególnym przypadkiem jest trójkąt egipski o stosunkach długości 3:4:5. Sprawdź czy trójkąt pitagorejski jest trójkątem egipskim.

d) Uwzględnij, że kolejność danych nie musi mieć znaczenia! Tzn. długość C użytkownik może podać jako pierwszą wartość. 
'''
#-------------------------------------------------------

A,B,C = input('Wprowadź trzy liczby naturalne\n'),input(),input()
A = int(A)
B = int(B)
C = int(C)

if A >= B and A >= C:
    if B >= C:
        Shortest = C
        Mid = B
        Longest = A
    else:
        Shortest = B
        Mid = C
        Longest = A
elif B >= C:
    if C >= A:
        Shortest = A
        Mid = C
        Longest = B
    else:
        Shortest = C
        Mid = A
        Longest = B
elif B >= A:
        Shortest = A
        Mid = B
        Longest = C
else:
        Shortest = B
        Mid = A
        Longest = C

print('Boki trójkąta od najdłuższego: {}, {}, {}' .format(Longest,Mid,Shortest))

if A + B > C:
    if A + C > B:
        if B + C > A:
            print ('Dla podanych liczb możliwe jest zbudowanie trójkąta.')
            if Shortest ** 2 + Mid ** 2 == Longest ** 2:
                print ('Dodatkowo będzie to trójkąt pitagoryjski.')
                if Shortest % 3 == 0 and Mid % 4 == 0 and Longest % 5 == 0:
                    print('Jest on też trójkątem egipskim.')  
            else:
                print('Jednakże nie jest to trójkąt pitagoryjski.')  
        else:
            print ('Dla podanych liczb nie można zbudować trójkąta.')
    else:
        print ('Dla podanych liczb nie można zbudować trójkąta.')
else:
    print ('Dla podanych liczb nie można zbudować trójkąta')


