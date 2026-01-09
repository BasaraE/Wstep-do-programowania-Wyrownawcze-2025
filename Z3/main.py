### ZAD11
from task_utils import show_tasks
### ZAD12
import task_utils as tu

### ZAD 13
def add_many_tasks(list_of_tasks, new_tasks):
    for new_task in new_tasks:
        tu.add_task(list_of_tasks, new_task)


tasks = ["pranie", "projekt", "zakupy", "siłownia"]

tu.add_task(tasks,"ride!")
show_tasks(tasks)

print("Nowa lista: ")
add_many_tasks(tasks, ["zmywarka", "odkurzanie", "daily-quest"])
show_tasks(tasks)

























#### Testowanie ZAD 1-9
#add_task(tasks, "ride!")
#show_tasks(tasks)
#remove_task(tasks, "obiad")
#remove_task(tasks, "projekt")
#print(has_task(tasks, "ride"))
#reset_tasks(tasks)
#show_tasks(get_urgent_tasks(tasks))


#archiwum = archive_tasks(tasks)
#show_tasks(archiwum)
#mark_done(tasks, "pranie")
#print("Tasks:")
#show_tasks(tasks)
#print("Archive:")
#show_tasks(archiwum)

# co sie stało z archiwum kiedo to z tasks zostało cos usunięte?



