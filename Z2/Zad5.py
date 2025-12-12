lista = []
for liczba in range(1, 11):
    lista.append(liczba)
    # print(lista)

# Zad 6
for element in lista:
    print(element)

# Zad 7
for element in lista:
    if element % 2 == 0:
        print(element)

# Zad 8
listaKW=[]

for element in lista:
    kw = element ** 2
    listaKW.append(kw)
    #print(listaKW)

# Zad 9
suma = sum(listaKW)
print(suma)
sumaITER=0

for element in listaKW:
    sumaITER += element

print(sumaITER)

# Zad 10
lista.append(7)
print(lista)
siedem = 0

for element in lista:
    if element == 7:
        siedem+=1
        print("Znalazłem 7")

print("Znalazłem", siedem, "x7")

# czy jest jakakolwiek "7" na liśice
if 7 in lista: print("Jest 7")

# siodemki = filter(7, lista)

# Zad 11
srednia = sumaITER / len(listaKW)
print(listaKW)
print(srednia)

for element in listaKW:
    if element >= srednia:
        print(element)

# Zad 12
odw = []
for element in listaKW:
    odw = [element] + odw

print(odw)
print(listaKW)

baza=listaKW
odw2 = []

while baza :
    element = baza.pop()
    odw2.append(element)
print(odw2)
print(baza)