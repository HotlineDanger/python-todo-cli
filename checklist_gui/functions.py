def get_todos(filepath="todos.txt"):
    """
    Returns a list of todos
    :param filepath:
    :return:
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_to_write, filepath="todos.txt"):
    """
        Write a list of todos
        :param todos_to_write:
        :param filepath:
        :return:
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_to_write)


if __name__ == "__main__":
    print("hello")
    print(get_todos())
