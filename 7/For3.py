'''Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
(np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
Następnie powitaj każdą osobę na liście.'''

#---------------------

Names = (input('Podaj liste imion rozdzielonych spacją\n'))
List = Names.split()

for Name in List:
    print('Cześć ' + Name)






      
