while True:
    # Get use input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    # Check if user action is "add"
    if "add" in user_action:
        todo = user_action[4:] + "\n"

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    # Check if user action is "show"
    if "show" in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip().title()
            row = f"{index + 1} - {item}"
            print(row)

    # Check if user action is "edit"
    if "edit" in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        number = int(input("Number of the todo to edit: "))
        number -= 1
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    # Check if user action is "complete"
    if 'complete' in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        number = int(input("Number of the todo to complete: "))
        number -= 1
        completed_todo = todos.pop(number)

        print(f'Todo "{completed_todo.strip().title()}" was removed from the list!')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        with open('complete.txt', 'w') as file:
            file.writelines(completed_todo)

    # Check if user action is "exit"
    if "exit" in user_action:
        print("Goodbye!")
        break

    # # Check if user action is "unknown"
    # if "_" not in user_action:
    #     print("Unknown command, please try again.")