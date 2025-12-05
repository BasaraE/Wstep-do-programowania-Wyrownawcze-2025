lista = []
## Zad5
for liczba in range(1,11):
    lista.append(liczba)
    print(lista)

print ("koniec for'a")

## Zad6
for element in lista:
    print(element)

## Zad7
for element in lista:
    if element % 2 == 0: ## dzielenie modulo - reszta z dzielenia
        print(element)
#    else:
#        print (element, "nieparzysta")

## Zad8
kwadraty = []
for element in lista:
    kwadraty.append(element**2)

print(kwadraty)

## Zad9
suma = sum(lista)
print(suma)

sumaListy = 0
for element in lista:
    print(sumaListy , "+", element, "=", end=" " )
    sumaListy += element
    print(sumaListy)

## Zad 10
print(7 in lista)
lista.append(7)
for element in lista:
    print(element, end=" ")
    if element == 7:
        print("znalazłem 7 na liście")
        break # znajdzie tylko pierwsza siódemkę

#alternatywa - flaga
lista.pop()
czy7 = False
for element in lista:
    if element == 7:
        czy7 = True
#    else: ## to jest niepotrzebne
#        czy7 = False

print("znalazłem", czy7)

#alternatywa - liczenie "7"
ile7 = 0
for element in lista:
    if element == 7:
        ile7 += 1
print("znalazłem", ile7, "siódemek")

## Zad 11
liczbaEl = len(lista)
srednia = suma/liczbaEl
wiekszeSrednia = []

for element in lista:
    if element > srednia:
        wiekszeSrednia.append(element)
        print(element)
    #else - nie robimy nic
print(wiekszeSrednia)