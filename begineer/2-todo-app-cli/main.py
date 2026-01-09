TODO_FILE = "todos.txt"
COMPLETE_FILE = "complete.txt"


def get_todos(filepath=TODO_FILE):
    try:
        with open(filepath, "r") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        return []


def write_todos(todos, filepath=TODO_FILE):
    with open(filepath, "w") as file:
        file.writelines(todo + "\n" for todo in todos)


def append_completed(todo, filepath=COMPLETE_FILE):
    with open(filepath, "a") as file:
        file.writelines(todo + "\n")


while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    # ================= ADD =================
    if user_action.startswith("add"):
        todo = user_action[4:].strip()

        if not todo:
            print("Todo cannot be empty.")
            continue

        todos = get_todos()
        todos.append(todo)
        write_todos(todos)
        print("Todo added.")


    # ================= SHOW =================
    elif user_action == "show":
        todos = get_todos()

        if not todos:
            print("No todos.")
        else:
            for i, todo in enumerate(todos, start=1):
                print(f"{i} - {todo.title()}")


    # ================= EDIT =================
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:].strip())
            todos = get_todos()
            index = number - 1

            if index < 0 or index >= len(todos):
                raise IndexError

            new_todo = input("Enter new todo: ").strip()
            if not new_todo:
                print("Todo cannot be empty.")
                continue

            todos[index] = new_todo
            write_todos(todos)
            print("Todo updated.")

        except ValueError:
            print("Use: edit <number>")
        except IndexError:
            print("There is no todo with that number.")


    # ================= COMPLETE =================
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:].strip())
            todos = get_todos()
            index = number - 1

            if index < 0 or index >= len(todos):
                raise IndexError

            completed = todos.pop(index)
            write_todos(todos)
            append_completed(completed)

            print(f'Todo "{completed.title()}" completed!')

        except ValueError:
            print("Use: complete <number>")
        except IndexError:
            print("There is no todo with that number.")


    # ================= EXIT =================
    elif user_action == "exit":
        print("Goodbye!")
        break

    else:
        print("Unknown command.")