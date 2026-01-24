# Z1

liczby = [2, 5, 76]
for liczba in liczby:
    print(liczba, end= " ")
print()

# Z2
liczby.append(986)
print(liczby)

# Z3
print(liczby[1])
print(liczby[3])
print(liczby[-1])

# Z4
dlugosc=len(liczby)
print(dlugosc)
print(liczby[dlugosc-1])

# Z5
nowa=[]
for i in range(1, 11):
    nowa.append(i)
print(nowa)

# Z7 #filtrowanie
for liczba in nowa:
    if liczba % 2 == 0:
        print(liczba)
# ver 2
print(list(filter(lambda x: x%2 == 0, nowa)))

# Z8
kwadraty=[]
# ver 1
for liczba in nowa:
    kwadraty.append(liczba**2)
print(kwadraty)

# ver 2 mapowanie map()
kwadraty = list(map(lambda x: x**2 , nowa))
print(kwadraty)

# Z9
suma=0
for liczba in nowa:
    suma += liczba
    # suma = suma + liczba
print(suma)

# Z10
print(7 in kwadraty)

# Z12
# ver1
a=0
for i in range(int(len(kwadraty)/2)):
    a = kwadraty[i]
    kwadraty[i]=kwadraty[len(kwadraty) - (i+1)]
    # [-(i+1)]
    kwadraty[len(kwadraty) - (i+1)] = a

print(kwadraty)

# ver2
odwr=[]
for liczba in kwadraty:
    odwr = [liczba] + odwr

print(odwr)

# Z13
unikaty=[]
lista=[1,4,3,5,4,1,6,7,2,2,8]

for liczba in lista:
    if liczba not in unikaty:
        unikaty.append(liczba)
print(unikaty)

# Z14
# liczby + unikaty

dwie = liczby + unikaty
print(dwie)

posortowana = sorted(dwie)
print(posortowana)

dwie.sort()
print(dwie)

#lista[0-3][0-1]
