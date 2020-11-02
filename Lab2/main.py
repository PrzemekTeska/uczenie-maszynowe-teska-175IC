import pandas as pd
from pandasgui import show

s = pd.read_csv('samochody1tys.csv')

show(s)

#Zamiana kolumn na wiersze
a = pd.melt(s)

show(a)

#Omija wiersze, jeśli jakaś kolumna nie ma wartości(w tym wypadku nie ma takich wierszy, ale warto wspomnieć o takiej funkcji)
b = s.dropna()

show(b)

#Sortowanie według przebiegu
c = s.sort_values('przebieg')

show(c)

#Zmiana nazwy kolumny z "cena" na "price"
d = s.rename(columns= {'cena':'price'})

show(d)

#Usunięcie kolumn "przebieg" i "cena"
e = s.drop(columns=['przebieg', 'cena'])

show(e)

#Wyświetlenie od 10 do 20 pozycji
f = s.iloc[10:20]

show(f)

#Wyświetlenie 5 ostatnich pozycji
g = s.tail(5)

show(g)

#Wyświetlenie 5 pierwszych pozycji
h = s.head(5)

show(h)

#Wyświetlenie tylko kolumny marka
i = s.filter(regex='marka')

show(i)

#Wyświetlenie 10 losowych wierszy
j = s.sample(10)

show(j)