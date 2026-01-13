import todo_config


def get_todos(filepath=todo_config.TODO_FILE):
    """Read todos from the specified file and return them as a list."""
    try:
        with open(filepath, "r") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        return []


def write_todos(todos, filepath=todo_config.TODO_FILE):
    """Write the list of todos to the specified file."""
    with open(filepath, "w") as file:
        file.writelines(todo + "\n" for todo in todos)


def append_completed(todo, filepath=todo_config.COMPLETE_FILE):
    with open(filepath, "a") as file:
        file.write(todo + "\n")
