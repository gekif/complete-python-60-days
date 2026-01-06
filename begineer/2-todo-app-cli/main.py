while True:
    # Get use input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    # Check if user action is "add"
    if "add" in user_action or "new" in user_action:
        todo = user_action[4:] + "\n"

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    # Check if user action is "show"
    elif "show" in user_action:
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
    elif "edit" in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        number = int(user_action[5:])
        number -= 1
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + "\n"

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    # Check if user action is "complete"
    elif 'complete' in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        number = int(user_action[9:])
        number -= 1
        completed_todo = todos.pop(number)

        print(f'Todo "{completed_todo.strip().title()}" was removed from the list!')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        with open('complete.txt', 'w') as file:
            file.writelines(completed_todo)

    # Check if user action is "exit"
    elif "exit" in user_action:
        print("Goodbye!")
        break

    # # Check if user action is "unknown"
    else:
        print("Unknown command, please try again.")