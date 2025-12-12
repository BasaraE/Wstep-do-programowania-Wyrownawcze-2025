lista = [1, 2, 3, 4, 5, 6]
print(lista)

for liczba in lista:
    print(liczba, end=" ")
print()

## Zad 2
lista.append(17)
print(lista)

lista.insert(3, 785)
print(lista)

## Zad 3
print(lista[0])
print(lista[4])
print(lista[-1])
print(lista[-2])
print(lista[2:5])
print(lista[ :5])
print(lista[5: ])
print(lista[ : : 2])

## Zad 3
print(lista)

dlugoscLEN= len(lista)
print(dlugoscLEN)
dlugoscITER=0

for liczba in lista:
    dlugoscITER += 1
    # dlugoscITER = dlugoscITER + 1
    # print(dlugoscITER)

print(dlugoscITER)


