import matplotlib.pyplot as plt

# przekazujemy dwa wektory wartości, najpierw dla wektora x, następnie y
# dodatkowo mamy tutaj przekazany parametr w postaci stringa, który określa styl wykresu
# dla pełnej listy sprawdź dokumentację pod adresem
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
# plt.subplot(211)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
# tutaj określamy listę parametrów w postaci [xmin, xmax, ymin, ymax]
plt.axis([0, 6, 0, 20])
#0, 6 -przedzial dla osi x; 0, 20 - przedzial dla osi y 
plt.show()
# plt.subplot(212)
# możemy też ustawiać różne kolory dla poszczególnych elementów nakładając na siebie dwa wykresy
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')

plt.axis([0, 6, 0, 20])
plt.show()