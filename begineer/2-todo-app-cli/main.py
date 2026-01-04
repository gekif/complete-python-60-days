while True:
    # Get use input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    match user_action:
        # Check if user action is "add"
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        # Check if user action is "show"
        case "show":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                item = item.strip().title()
                row = f"{index + 1} - {item}"
                print(row)

        # Check if user action is "edit"
        case "edit":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            number = int(input("Number of the todo to edit: "))
            number -= 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        # Check if user action is "complete"
        case 'complete':
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            number = int(input("Number of the todo to complete: "))
            number -= 1
            completed_todo = todos.pop(number)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

            file = open('complete.txt', 'w')
            file.writelines(completed_todo)
            file.close()

        # Check if user action is "exit"
        case "exit":
            print("Goodbye!")
            break

        # Check if user action is "unknown"
        case _:
            print("Unknown command, please try again.")