def show_tasks(lista_zadan):
    for zadanie in lista_zadan:
        print(zadanie)

def add_task(lista_zadan, nowe_zadanie):
    lista_zadan.append(nowe_zadanie)

# funkcja przeniesiona:
def has_task(lista_zadan, zadanie):
    #return len(lista_zadan) > 0 # czy ma jakiekolwiek wpisy
    return zadanie in lista_zadan # czy ma konkretny wpis

def remove_task(lista_zadan, zadanie):
    if has_task(lista_zadan, zadanie):
        lista_zadan.remove(zadanie)
    else:
        print("zadanie nie znajduje się na liście")

def count_tasks(lista_zadan):
    return len(lista_zadan)

def reset_tasks(lista_zadan):
    lista_zadan.clear()

def get_urgent_tasks(lista_zadan):
    # Metoda 1
    #urgent = []
    #for zadanie in lista_zadan:
    #    if "!" in zadanie:
    #        urgent.append(zadanie)
    #return urgent

    # Metoda 2
    def filtr(x):
        if "!" in x:
            return True
        else:
            return False

    urgent = list(filter(filtr, lista_zadan))
    # filter zwraca iterator(wskaźnik) zamiast gotowej listy
    return urgent

def mark_done (lista_zadan, zadanie):
    remove_task(lista_zadan, zadanie)

def archive_tasks(lista_zadan):
    return lista_zadan.copy()
