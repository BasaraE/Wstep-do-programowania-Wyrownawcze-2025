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
