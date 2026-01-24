from task_utilis import show_tasks
import task_utilis as tu

tasks = ["pranie", "projekt", "zakupy", "siłownia!"]

tu.add_task(tasks, "rajd")
def add_many_tasks(lista, zadania):
    for zadanie in zadania:
        tu.add_task(lista, zadanie)

new=["lv", "kowal", "teleport"]
add_many_tasks(tasks, new)

show_tasks(tasks)