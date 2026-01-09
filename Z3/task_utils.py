### ZAD1
def show_tasks(list_of_tasks):
    for task in list_of_tasks:
        print(task)

### ZAD2
def add_task(list_of_tasks, new_task):
    list_of_tasks.append(new_task)

### ZAD3
def remove_task(list_of_tasks, del_task):
    if has_task(list_of_tasks, del_task):
        list_of_tasks.remove(del_task)
    else:
        print(f"Lista nie zawiera {del_task}")
    # zwrócić informacje jeśli nie ma elementu na liscie albo "przejsć dalej"

### ZAD 4
# długość listy

## ZAD5 # powinno być przed ZAD3
def has_task(list_of_tasks, task):
    #if (task in list_of_tasks):
    #    return True
    #else:
    #    return False
    return task in list_of_tasks

### ZAD6
def reset_tasks(list_of_tasks):
    list_of_tasks.clear()

### ZAD7
def get_urgent_tasks(list_of_tasks):
    urgent_tasks = []
    for task in list_of_tasks:
        if '!' in task:
            urgent_tasks.append(task)
    return urgent_tasks

### ZAD8
def mark_done(list_of_tasks, task):
    remove_task(list_of_tasks, task)
    # dodanie jakiegoś oznaczenia np. znak specjalny

### ZAD9
def archive_tasks(list_of_tasks):
    return list_of_tasks
