FILENAME = "todos.txt"

def humane_list_display(lista):
    lista = [f"{index + 1}-{item.strip()}" for index, item in enumerate(lista)]
    return lista


def get_todos(filename = FILENAME):
    with open(filename, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath = FILENAME):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)