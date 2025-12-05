#Zad 1
lista = [1,7,13]
# cała struktura listy
print(lista)
# konkretny element listy
print(lista[0])
# wszystkie elementy listy
for element in lista:
    print(element, end=" ")
print("")

#Zad2
#dodaj element na końcu
lista.append(31)
# dodaj element na pozycji i przesuń resztę (bez strat)
lista.insert(2, 11)
# zamiana elementu na liście
lista[3] = 17
print(lista)

#Zad3
# ostatni: dokładny index
liczbaElementow = len(lista)  ## Zad4
indexOstatniego = liczbaElementow - 1
print(lista[indexOstatniego])  # lista[4]

# ostatni: index uproszczony
print(lista[-1])

# ostatni: ze zmianą zawartosci listy (usunięciem elementu)
print(lista.pop())
print(lista)

