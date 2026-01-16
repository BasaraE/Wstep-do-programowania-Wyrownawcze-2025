tasks = ["pranie", "projekt!", "zakupy", "siłownia"]

def show_tasks(lista_zadan):
    for zadanie in lista_zadan:
        print(zadanie)

    # print (lista_zadan) -> ["pranie", "projekt", "zakupy", "siłownia"]
#show_tasks(tasks)

def add_task(lista_zadan, nowe_zadanie):
    lista_zadan.append(nowe_zadanie)

#add_task(tasks, "odkurzanie")
#show_tasks(tasks)

# funkcja przeniesiona:
def has_task(lista_zadan, zadanie):
    #return len(lista_zadan) > 0 # czy ma jakiekolwiek wpisy
    return zadanie in lista_zadan # czy ma konkretny wpis


def remove_task(lista_zadan, zadanie):
    if has_task(lista_zadan, zadanie):
        lista_zadan.remove(zadanie)
    else:
        print("zadanie nie znajduje się na liście")

#remove_task(tasks, "rajd")
#show_tasks(tasks)
#lista=[1]

def count_tasks(lista_zadan):
    return len(lista_zadan)

#print(f"lista składa się z {count_tasks(tasks)} zadań/nia")

#print(has_task(tasks,"rajd" ))

def reset_tasks(lista_zadan):
    lista_zadan.clear()

# reset_tasks(tasks)
# tasks = []
# tasks = reset_tasks(tasks)
# print(tasks)

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

#print(get_urgent_tasks(tasks))
#show_tasks(get_urgent_tasks(tasks))

def mark_done (lista_zadan, zadanie):
    remove_task(lista_zadan, zadanie)

def archive_tasks(lista_zadan):
    return lista_zadan.copy()

tasksArchive = archive_tasks(tasks)
remove_task(tasks, "pranie")
print(tasksArchive)
print(tasks)