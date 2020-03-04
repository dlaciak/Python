'''
Wyobraź sobie, że jesteś bioinformatykiem i otrzymujesz kod genetyczny do analizy.

Kod DNA składa się z 4 zasad azotowych: adeniny(A), cytozyny(D), guaniny(G), tyminy(T).
Idealny kod DNA wygląda następująco: TGCACGATCATGTCTACTATCCTCTCTATGGTGGGGTT.
Zdarza się, jednak, że kod zawiera małe jak i duże litery.
Kolejny problem to maszyny sekwencjonujące nie są wolne od błędów.
W zależności od maszyny błędy sekwencjonowania mogą zostać zamienione na znak – czy literę N.

    W jaki sposób łatwo rozpoznasz, że otrzymany kod DNA zawiera błędy?


    Skopiuj kod genetyczny do swojego skryptu i zapisz jako DNA = ACTG...
    Policz ile razy występuje w kodzie każda zasada azotowa – adenina, cytozyna, guanina, tymina.

Na pewno zauważysz błędy sekwencjonowania – znaki, które nie są żadną z 4 zasad.
W panice szukasz pliku z dokumentacją.
Ufff… znalazł się!
Co więcej, w dokumentacji pojawił się następujący zapis:

gdy jakość sekwencji nie pozwala dokładnie odczytać rodzaju zasady azotowej wstawiany jest znak „-”
Natomiast, gdy laser sczytujący ześlizgnie się, wstawiane są litery „N”,
jednocześnie ostatnia wartość zasady jest ponownie odczytywana bez ubytku zasady w tym miejscu.

Co za przydatna informacja!

    Policz wystąpienia sekwencji GAGA i zamień je na AGAG
    Znajdź miejsce (indeks) w łańcuchu, gdzie występuje 7 guanin z rzędu
    Znajdź miejsce (indeks) , gdzie od końca łańcucha występuje 6 cytozyn
    Policz ile razy w kodzie pojawiła się sekwencja CTGAAA
    W sekwencji CTGAAA czasem mutuje ostania litera A, wówczas jakość ostatniej litery może być wątplia. Ile sekwencji znajdziesz, jeśli weźmiesz pod uwagę wątpliwą, ostatnią adeninę?
    Oczyść DNA z wszystkich błędów. Na podstawie czystej nici utwórz odpowiadającą jej nić RNA (nić RNA w miejscu tyminy będzie mieć uracyl (U))

'''

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

DNA = '''ACTGTGCTGACTCCCGGTGCTGCCGCTGCCATAGCTAAAGCCCGGGTCCTGGTAGGCAGGCGGGAAGCAG
GGTGGGGGTCCCGGGTACTGGTAGGGGTAGCCCTGACCCAGAGGCGGGGGGGCAGCCGGGTGGGGCAGCG
GGGCCAGCGTGTCCTGAA-CGAAGTCCCACTGGAGCCACTGTTGAGGTTCAGGGTGGCGAGATCTGGCGG
NNNAGGGTAGGTGAGGGCCGCGGAGGGGCCTCCGGCGTTCCCCTCCCCCCCGCCCTGAAACCCGAAGCCC
CCACTCACTGCTGCAGAGATCCCCTGAAAACGTAGTAGCACTGCTCgagacAGGTGATCTGTTGACCTGA
AACCGCAGGAAGCCGTGCTTCAGCAAGCTGCTGGCGTACTTCCGGGCCT---GCCGCTCCTTGAAGCCCT
CCACGTGTGTGTACAGCCAGTCCACCACGTCCGCCCCTGGCCGGCACCAGCGGTCAGCCCGCAGCCTCGA
GGCAAGCAGCCCTGCCNNTGGCACTATCCGC-CGCGGGGACGGCCACTCACCGATGACGGCATNNGCGAT
GGTGATCTTGAGCCACATGCGGTCGCGGATCTCCAGTCCCGAG---GGCAGCTGCATGACCCGGACGACG
GCGCTCATGTCACtcaccgtcagcggcgcctcttccagCCAGCTCTGCAAAGCACAGACAGCCCCGCTTC
GCCCCAGCATCTGAAAGCGGGGGACTCggcAcgCTGCACCCCCAGGGGAGCCTCTGGGCAGAGCCTGCGC
CAGGGCGCAAGCTGGACGGTGCGTGACAGCAGGGCCCCGGCCCACTGCAGGATGCACCCCCGTGAGGCTG
GGGCGTGAGCAGGGGGGTTGGACAtttAGTCTCCCACTTCTACAGACACTTTTCATCAGGATCCTAGGCA
CAAACTGGGCTGAAACCCCACCCTGCAGACCAGGAAGTAATGAGAACAGGGCAGGCCCCTTCCCCTCNNC
GCATGCC-CACCCGAGAGCGCAGGCTGTTAGTCGTGTTAATGGCAGGAAGCAGAATGGAGACCTGGCCCC
TGCCTCTGAA-CCGTGGGTGCTCaactggctaGCCCTACGTACATCCCCTGTTCcggCCAACACACAGAC
ATGAGCAGGATGGGCTGCACAAGGTGGGCACGGGTGCCTGTGCACACGTCTGTGCAGGGAGTTGGGGACA
GGCAACACACACGTGTCACAGCCCCATGACGGggcaattgcGCCATGCTGGCTGAATGGCAGAGACGCCC
CTCCAAGCCTCGGTTTCTGCTGGGGCCCTCAGGAGCTGCCACTTACGTGGAGCACCAGGCACGGAGCTGG
TTAGTGAGGAGGAGCTGGTGCGCGTGACGGCGCTGGAGCAGGGACTCGTACCGTAGCGGGGCAGGGCNNN
TGTCAGTGCCGCCGTGTGGtcagcggcgatCGGCG-GGTCGATGGGCCGCACCGGGTCAGCTGGGTGNAG
ACACGTGGCGATGACAGGCGGACAGATGGACAGGGTGGGAGGGCAGGGTGCAGGGCACAGAGGAGAGAGG
CCTTCAGGCTAGGTAGGCGCCCCCTCCCCATCCCGccccGTGTGCCCCGAGGGCCACTCACCCCGTGGGA
CGGTGAAGTAGCTTCG-GGCGTTGGGTCCAGCACTTGGCCACAGTGAGGCTGNAAATGGCTGCAGGAACG
GTGGTCCCCCCGCAAGGCCCCCATGGTCCCACCTCCCTGCCTGGCCCCTCCCGCTCCAGCGCCNCCAGCC'''

DNA = DNA.replace(' ','')
DNA = DNA.upper()

print('Adenina wystąpiła {} razy' .format(DNA.count('A')))
print('cytozyna wystąpiła {} razy' .format(DNA.count('C')))
print('Guanina wystąpiła {} razy' .format(DNA.count('G')))
print('Tymina wystąpiła {} razy' .format(DNA.count('T')))
CorrectedDNA = DNA.replace('N','').upper()
print('Sekwencja GAGA pojawia się {} razy' .format(CorrectedDNA.count('GAGA')))
CorrectedDNA = DNA.replace('GAGA','AGAG').upper()

print('Indeks 7 guanin z rzędu to {}' .format(CorrectedDNA.find('GGGGGGG')))
print('Indeks 6 cytozyn z rzędu licząc od końca to {}' .format(CorrectedDNA.rfind('CCCCCC')))
print('Sekwencja CTGAAA pojawia się {} razy' .format(CorrectedDNA.count('CTGAAA')))
print('Sekwencja CTGAAA lub CTGAA- pojawia się {} razy' .format(CorrectedDNA.count('CTGAAA')+CorrectedDNA.count('CTGAA-')))

RNA = CorrectedDNA.replace('-','').replace('T','U')







