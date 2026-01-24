tasks = ["pranie", "projekt", "zakupy", "siłownia!"]

#1
def show_tasks(lista):
    for zadanie in lista:
        print(zadanie)
#2
def add_task(lista, nowe_zadanie):
    lista.append(nowe_zadanie)
    #lista += [nowe_zadanie]

add_task(tasks, "odkurzanie")
#3
def remove_task(lista, zadanie):
    if zadanie in lista:
        lista.remove(zadanie)
    else:
        print("Nie ma takiego zadania na liście")

remove_task(tasks, "spacer")
show_tasks(tasks)

#4
def count_tasks(lista):
    return len(tasks)

print(count_tasks(tasks))

#5
def has_task(lista, zadanie):
#    if zadanie in lista:
#        return True
#    else:
#        return False
    return zadanie in lista

print(has_task(tasks, "obiad"))

# 3 EDIT
def remove_task_edit(lista, zadanie):
    if has_task(lista, zadanie):
        lista.remove(zadanie)
    else:
        print("Nie ma takiego zadania na liście")

#remove_task_edit(tasks, "odkurzanie")
#show_tasks(tasks)

# 6
def reset_tasks(lista):
    # ver 1
    #lista = []
    #return lista

    # ver 2
    lista.clear()


#reset_tasks(tasks)
#show_tasks(tasks)

# 7

def get_urgent_tasks(lista):
    pilne = []
    #ver 1
#    for zadanie in lista:
#       print(zadanie)
#        print("!" in zadanie)
#        if "!" in zadanie:
#            pilne.append(zadanie)
#            print(pilne)

    # ver 2 - filter()
    def filtr (x):
        if "!" in x:
            return True
        else:
            return False

    pilne = list(filter(filtr,lista))
    print(pilne)

    return pilne

urgent = get_urgent_tasks(tasks)
show_tasks(urgent)

# 8
def mark_down(lista, zadanie):
    remove_task(lista, zadanie)

#9
def archive_tasks(lista):

    return lista.copy()

archive = archive_tasks(tasks)
show_tasks(archive)

mark_down(tasks,"odkurzanie")
show_tasks(tasks)
show_tasks(archive)