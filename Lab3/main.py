import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure
from bokeh.layouts import gridplot
from bokeh.io import export_png

my_list = ['my', 'list', 'is', 'excellent']

# Pierwszy cheat sheet

# index() - zwraca index konkretnej wartości w liście
print(my_list.index('excellent'))

# sort() - sortowanie listy
my_list.sort()
print(my_list)

# reverse() - odwraca listę
my_list.reverse()
print(my_list)

# append() - dodanie wartości do listy
my_list.append('!')
print(my_list)

# remove() - usunięcie wartości z listy
my_list.remove('my')
print(my_list)

#################################################

# Drugi cheat sheet

a = 16
b = 4

# multiply() - mnożenie dwóch liczb
print(np.multiply(a, b))

# sqrt() - pierwiastek z liczby
print(np.sqrt(a))

# add() - dodawanie dwóch liczb
print(np.add(a, b))

# substract() - odejmowanie dwóch liczb
print(np.subtract(a, b))

# divide() - dzielenie dwóch liczb
print(np.divide(a, b))

#################################################

# Trzeci cheat sheet

A = np.matrix(np.random.random((2, 2)))
B = np.asmatrix(b)
C = np.mat(np.random.random((10, 5)))
D = np.mat([[3, 4], [5, 6]])

print(D)

# T - transpozycja macierzy
print(D.T)

# add() - dodawanie macierzy
print(np.add(A, D))

# substract() - odejmowanie macierzy
print(np.subtract(A, D))

# divide() - dzielenie macierzy
print(np.divide(A, D))

# multiply() - mnożenie macierzy
print(np.multiply(D, A))

#################################################

# Czwarty cheat sheet

s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])

# min() - zwraca najmniejszą wartość
print(s.min())

# sum() - sumuje wartości
print(s.sum())

# max() - zwraca największą wartość
print(s.max())

# mean() - średnia wartości
print(s.mean())

# describe() - opis dataframe
print(s.describe())

#################################################

# Piąty cheat sheet

# Algorym k średnich
k_means = KMeans(n_clusters=3, random_state=0)

# Uczenie i testowanie danych
X = np.random.random((11, 11))
y = np.array(['M', 'M', 'F', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'F'])

X_train, X_test, y_train, y_test = train_test_split(X, y)

# Standaryzacja
scaler = StandardScaler().fit(X_train)
standardized_X = scaler.transform(X_train)
standardized_X_test = scaler.transform(X_test)

# Normalizacja
scaler = Normalizer().fit(X_train)
normalized_X = scaler.transform(X_train)
normalized_X_test = scaler.transform(X_test)

# Generowanie wielomianu
poly = PolynomialFeatures(5)
poly.fit_transform(X)

#################################################

# Szósty cheat sheet
x = np.linspace(0, 10, 100)
y = np.cos(x)

fig = plt.figure()
fig2 = plt.figure(figsize=plt.figaspect(2.0))

fig.add_subplot()
ax1 = fig.add_subplot(221)  # row-col-num
ax3 = fig.add_subplot(212)
fig3, axes = plt.subplots(nrows=2, ncols=2)
fig4, axes2 = plt.subplots(ncols=3)

fig, ax = plt.subplots()
axes[0, 0].bar([1, 2, 3], [3, 4, 5])  # Rysowanie pionowych prostokątów ze stałą szerokością
axes[1, 0].barh([0.5, 1, 2.5], [0, 1, 2])  # Rysowanie poziomych prostokątów ze stałą wysokością
axes[1, 1].axhline(0.45)  # Rysowanie poziomej linii przez osie
axes[0, 1].axvline(0.65)  # Rysowanie pionowej linii przez osie
ax.fill(x, y, color='blue')  # Rysowanie wypełnionego wielokąta

#################################################

# Siódmy cheat sheet

iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")

# Wykres punktowy z jedną zmienną
sns.stripplot(x="species",
              y="petal_length",
              data=iris)

# Wykres słupkowy
sns.barplot(x="sex",
            y="survived",
            hue="class",
            data=titanic)

# Tytuł wykresu
plt.title("A Title")

# Ustawienie limitu osi y
plt.ylim(0, 100)

# Ustawienie limitu osi x
plt.xlim(0, 10)

#################################################

# Ósmy cheat sheet
p = figure(tools='box_select')
p1 = figure(plot_width=300, tools='pan,box_zoom')
p2 = figure(plot_width=300, plot_height=300,
            x_range=(0, 8), y_range=(0, 8))
p3 = figure()

# Lokalizacja legendy wewnątrz wykresu
p.legend.location = 'bottom_left'

# Orientacja legendy wykresu
p.legend.orientation = "horizontal"
p.legend.orientation = "vertical"

# Obramówka i tło legendy wykresu
p.legend.border_line_color = "navy"
p.legend.background_fill_color = "white"

# Układ typu grid
row1 = [p1, p2]
row2 = [p3]
layout = gridplot([[p1, p2], [p3]])

# Export do pliku .png
export_png(p, filename="plot.png")
