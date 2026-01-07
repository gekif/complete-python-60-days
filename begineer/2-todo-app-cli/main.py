while True:
    # Get use input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    # Check if user action is "add"
    if user_action.startswith("add"):
        todo = user_action[4:].strip()

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    # Check if user action is "show"
    elif user_action.startswith("show"):
        try:
            with open("todos.txt", "r") as file:
                todos = file.readlines()

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
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            number = int(user_action[5:].strip())
            index = number - 1

            # 🔴 VALIDASI INDEX DI SINI
            if index < 0 or index >= len(todos):
                raise IndexError

            # ✅ BARU MINTA INPUT JIKA INDEX VALID
            new_todo = input("Enter new todo: ")
            todos[index] = new_todo + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        except ValueError:
            print("Your command is not valid. Use: edit <number>")

        except IndexError:
            print("There is no todo with that number.")


    # Check if user action is "complete"
    elif user_action.startswith("complete"):
        try:
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            number = int(user_action[9:].strip())
            index = number - 1

            # 🔴 VALIDASI INDEX
            if index < 0 or index >= len(todos):
                raise IndexError

            completed_todo = todos.pop(index)

            print(f'Todo "{completed_todo.strip().title()}" was removed from the list!')

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            with open("complete.txt", "a") as file:
                file.write(completed_todo)

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