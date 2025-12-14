# Zad1
lista = [1,2,3]
# struktura
print(lista)
# kolejne elementy
for el in lista:
    print(el, end=" ")
print()

# Zad2
# dodaj na końcu
lista.append(77)
print(lista)

# dodaj na konkretnej pozycji
lista.insert(2, 8)
print(lista)

# Zad 3
print(lista[0])
print(lista[3])
print(lista[-1])
print(lista[-3])

# Zad 4
dlugoscListy = len(lista)
print(dlugoscListy)
print(lista[dlugoscListy-1])

# Zad 5
lista2 = []

for liczba in range(1,11):
    lista2.append(liczba)
print(lista2)

# Zad 7
for el in lista2:
    if el%2 == 0:
        print(el)

#filtrowanie

# Zad 8
listaKW=[]
for el in lista2:
    listaKW.append(el**2)
print(listaKW)

#mapowanie

# Zad 9
suma = 0
for el in lista:
    suma += el
    print(suma)

#sumowanie

# Zad 10
lista2.append(7)
print(lista2)
licz7 = 0
for el in lista2:
    if el == 7:
        # licz7 += 1
        licz7 = licz7 + 1

print(f"Znalazłem {licz7} x7")

# Zad 11
print(lista)
srednia = suma / dlugoscListy
print(srednia)

for el in lista:
    if el > srednia:
        print(el)

# Zad 12
polowa=0
if dlugoscListy % 2 ==0:
    polowa = int(dlugoscListy / 2)
else:
    polowa = int((dlugoscListy-1) / 2)

for i in range(polowa):
    print(lista[i])
    print(lista[-(i+1)])
    #znak = lista[i]
    #lista[i] = lista[-(i+1)]
    #lista[-(i+1)] = znak
    lista[i], lista[-(i+1)] = lista[-(i+1)], lista[i]

print(lista)

# Zad 13
print(lista2)
slownik = {}
# slownik = {znak : liczba wyst.}

for el in lista2:
    slownik[el] = 0
print(slownik)

for i in range(len(lista2)):
    wartosc=lista2[i]
    if slownik[wartosc]==0:
        slownik[wartosc]+=1
    else:
        lista2[i]='@'
        # jak usunąć element z listy na stałe?
print(slownik)
print(lista2)

# Zad 14
polaczone = lista + listaKW
print(polaczone)
print(sorted(polaczone))
print(polaczone.sort())
print(polaczone)

# Zad 15
zakupy = ["chleb","baton","jabłko","chipsy","banan","paluszki"]
niezdrowe = ["baton","chipsy","paluszki"]
zdrowe=[]
# NOPE zdrowe = zakupy - niezdrowe

for el in zakupy:
    if el not in niezdrowe:
        zdrowe.append(el)
print(zdrowe)

# Zad 16
wagi = [2.5,15,1.2,6,12,3.3]
doKontroli = []
for el in wagi:
    if el > 10:
        doKontroli.append(el)
print(doKontroli)

# Zad 17
kolejka = ["Anna","Dima","Olia","Marko","Sara"]

while (kolejka):
    print(f"obsługuwany: {kolejka.pop()}")

print(kolejka)