todos = []

while True:
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display":
            for item in todos:
                item = item.title()
                print(item)
        case "exit":
            print("Goodbye!")
            break
        case _:
            print("Unknown command, please try again.")