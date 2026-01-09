def get_todos(filepath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath, todos_local):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_local)

def complete_todos(filepath, completed_todos_local):
    with open(filepath, "a") as file_local:
        file_local.writelines(completed_todos_local)


while True:
    # Get use input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    # Check if user action is "add"
    if user_action.startswith("add"):
        todo = user_action[4:].strip()

        todos = get_todos("todos.txt")

        todos.append(todo + "\n")

        write_todos("todos.txt", todos)

    # Check if user action is "show"
    elif user_action.startswith("show"):
        try:
            todos = get_todos("todos.txt")

            if not todos:
                print("No todos")
            else:
                for index, item in enumerate(todos):
                    item = item.strip().title()
                    row = f"{index + 1} - {item}"
                    print(row)

        except FileNotFoundError:
            print("No todos")

    # Check if user action is "edit"
    elif user_action.startswith("edit"):
        try:
            todos = get_todos("todos.txt")

            number = int(user_action[5:].strip())
            index = number - 1

            # 🔴 VALIDASI INDEX DI SINI
            if index < 0 or index >= len(todos):
                raise IndexError

            # ✅ BARU MINTA INPUT JIKA INDEX VALID
            new_todo = input("Enter new todo: ")
            todos[index] = new_todo + "\n"

            write_todos("todos.txt", todos)

        except ValueError:
            print("Your command is not valid. Use: edit <number>")

        except IndexError:
            print("There is no todo with that number.")


    # Check if user action is "complete"
    elif user_action.startswith("complete"):
        try:
            todos = get_todos("todos.txt")

            number = int(user_action[9:].strip())
            index = number - 1

            # 🔴 VALIDASI INDEX
            if index < 0 or index >= len(todos):
                raise IndexError

            completed_todo = todos.pop(index)

            print(f'Todo "{completed_todo.strip().title()}" was removed from the list!')

            write_todos("todos.txt", todos)
            complete_todos("complete.txt", completed_todo)

        except ValueError:
            print("Your command is not valid. Use: complete <number>")

        except IndexError:
            print("There is no todo with that number.")


    # Check if user action is "exit"
    elif user_action.startswith("exit"):
        print("Goodbye!")
        break

    # # Check if user action is "unknown"
    else:
        print("Unknown command, please try again.")