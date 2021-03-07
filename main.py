from math import *
import sys as system

# Zad 1. Napisz skrypt, w którym tworzysz listę ulubionych sportów,
# odwróć ją a następnie dodaj mniej lubiane sporty na sam koniec.

print("Zad 1.")
lista1 = ["siatkowka", "koszykowka", "baseball", "tenis"]
print(lista1)
lista1.reverse()
print(lista1)
lista1.extend(("pilka nozna", "football", "wodne polo"))
print(lista1)

# Zad 2. Stwórz słownik skrótów powszechnie używanych w gazetach lub artykułach internetowych.
# Jako klucz przyjmij skrót danego słowa, wartość to rozwinięcie tego skrótu.

print("Zad 2.")
slownik1 = {"LOL": "Laugh out loud", "gz": "congratulation", "gj": "good job", "wp": "well played"}
print(slownik1)

# Zad 3. Stwórz słownik z ulubionymi grami komputerowymi. Pomyśl, co może być kluczem a co wartością w takim słowniku.
# Policz liczbę elementów w słowniku.

print("Zad 3.")
slownik2 = {"FPS": "Halo", "RPG": "Fallout", "RTS": "Age of Empires II", "Survival": "7 Days to die"}
print(slownik2)
print("Liczba elementow: ", len(slownik2))

# Zad 4. Napisz skrypt, który pobiera od użytkownika zdanie i liczy wystąpienia litery a.
# Użyj funkcji input.

print("Zad 4.")
zdanie1 = input("Podaj zdanie a policze ilosc liter a w tym zdaniu: ")
print(zdanie1.count("a") + zdanie1.count("A"))

# Zad 5. Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: ab + c.
# Użyj instrukcji readline() i write()).

system.stdout.write("Zad 5. Podaj 1wsza liczbe: ")
l1 = system.stdin.readline()
system.stdout.write("Podaj 2ga liczbe: ")
l2 = system.stdin.readline()
system.stdout.write("Podaj 3cia liczbe: ")
l3 = system.stdin.readline()
l1 = float(l1)
l2 = float(l2)
l3 = float(l3)
wynik1 = pow(l1, l2) + l3
system.stdout.write("a^b + c = %f\n" % wynik1)

# Zad 6. Wczytaj trzy liczby całkowite a,b,c i sprawdź, która z nich jest największa.
# W zależności od wyniku wyświetl odpowiedni komunikat. Użyj zagnieżdżeń.

print("Zad 6.")
a1 = input("Podaj liczbe a: ")
b1 = input("Podaj liczbe b: ")
c1 = input("Podaj liczbe c: ")

if a1 >= b1:
    if a1 > c1:
        print("Najwieksza liczba to a = ", a1)
    else:
        print("Najwieksza liczba to c = ", c1)
elif b1 >= a1:
    if b1 > c1:
        print("Najwieksza liczba to b = ", b1)
    else:
        print("Najwieksza liczba to c = ", c1)

# Zad 7. Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float.
# Następnie za pomocą użycia pętli for podnieś każdą liczbę do kwadratu.

print("Zad 7.")
lista2 = [4, 6, 2, 3.5, 6.6, 3.14]
print(lista2)
lista3 = []
for x in lista2:
    wynik2 = x ** 2
    lista3.append(wynik2)
print(lista3)

# Zad 8. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb,
# następnie dodaje do listy tylko parzyste liczby.

print("Zad 8. Wprowadz 10 liczb a dodam parzyste")
ilosc = 0
lista4 = []
while ilosc != 10:
    l4 = input()
    ilosc += 1
    if int(l4) % 2 == 0:
        lista4.append(l4)
print(lista4)

# Zad 9. Napisz skrypt, który rysuje następującą literę
# EEEEEE
# E
# EEEEEE
# E
# EEEEEE
# Etapy wykonania ćwiczenia:
# Deklarujemy jedną następującą listę [1,2,3,4,5].
# Następnie za pomocą pętli i instrukcji warunkowej wykonujemy odpowiednie działania.
# Trzeba wykorzystać zagnieżdżenia.

print("Zad 9.")
lista5 = [1, 2, 3, 4, 5]

for x in lista5:
    if x == 1 or x == 3 or x == 5:
        print("EEEEEE")
    else:
        print("E")


# Zad. 10
# Napisz skrypt, który liczy pierwiastek z liczby podanej przez użytkownika
# jeśli użytkownik poda wartość ujemną to powinien być wyłapany błąd.

liczba = input("Zad 10. Podaj liczbe a spierwiastkuje ja: ")
liczba = float(liczba)
try:
    liczba = sqrt(liczba)
    print("Wynik: ", liczba)
except ValueError:
    print("Wprowadzona zla liczbe")
