while True:
    # Get use input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    match user_action:
        # Check if user action is "add"
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        # Check if user action is "show"
        case "show":
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip().title()
                row = f"{index + 1} - {item}"
                print(row)

        # Check if user action is "edit"
        case "edit":
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            number = int(input("Number of the todo to edit: "))
            number -= 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        # Check if user action is "complete"
        case 'complete':
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            number = int(input("Number of the todo to complete: "))
            number -= 1
            completed_todo = todos.pop(number)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            with open('complete.txt', 'w') as file:
                file.writelines(completed_todo)

        # Check if user action is "exit"
        case "exit":
            print("Goodbye!")
            break

        # Check if user action is "unknown"
        case _:
            print("Unknown command, please try again.")