FILEPATH = "todos.txt"
def get_todos(filepath="todos.txt"):
    """Read a text file and return the list
    of to-dos items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """Write the todos items list in the text file"""
    with open(filepath, 'w') as file:
        # file opbjects to open the document in a specific directory w=write r=read
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())

