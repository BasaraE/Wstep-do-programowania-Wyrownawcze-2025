##Zad11
# from task_utils import show_tasks
##Zad12
import task_utils as tu

# Zad 13
def add_many_tasks(lista_zadan, lista_nowych_zadan):
    for zadanie in lista_nowych_zadan:
        tu.add_task(lista_zadan, zadanie)

#Zad 14
def tasks_report(lista_zadan, zadanie = "projekt"):
    length = tu.count_tasks(lista_zadan)
    length_urgent = tu.count_tasks(tu.get_urgent_tasks(lista_zadan))
    projekt = tu.has_task(lista_zadan, zadanie)

    print("długość listy zadań:", length)
    print("Liczba zadań pilnych:", length_urgent)

    if projekt: print(f"zadanie {zadanie} znajduje się na liście")
    else: print(f"zadanie {zadanie} NIE znajduje się na liście")
    # sprawdza czy dokładnie "projekt" jest na liście i jest ale "projekt!"
    # nie jest to pełna funkcjonalność !!!


tasks = ["pranie", "projekt!", "zakupy", "siłownia!"]
#Zad 11
#show_tasks(tasks)
#zad 12
#task_utils.show_tasks(tasks)
#tu.show_tasks(tasks)
#Zad 13
nowe=["spacer", "wykład!"]
add_many_tasks(tasks, nowe)
#tu.show_tasks(tasks)

#Zad 14
tasks_report(tasks)