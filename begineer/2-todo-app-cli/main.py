todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display":
            for index, item in enumerate(todos):
                item = item.title()
                print(f"{index + 1} - {item}")
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number -= 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            number -= 1
            todos.pop(number)
        case "exit":
            print("Goodbye!")
            break
        case _:
            print("Unknown command, please try again.")