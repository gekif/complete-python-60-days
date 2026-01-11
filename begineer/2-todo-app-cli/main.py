from todo_functions import get_todos, write_todos, append_completed

def main():
    while True:
        user_action = input("Type add, show, edit, complete, delete or exit: ").strip()

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

        # ================= DELETE =================
        elif user_action.startswith("delete"):
            try:
                number = int(user_action[7:].strip())
                todos = get_todos()
                index = number - 1

                if index < 0 or index >= len(todos):
                    raise IndexError

                delete = todos.pop(index)
                write_todos(todos)

                print(f'Todo "{delete.title()}" deleted!')

            except ValueError:
                print("Use: delete <number>")
            except IndexError:
                print("There is no todo with that number.")


        # ================= EXIT =================
        elif user_action == "exit":
            print("Goodbye!")
            break

        else:

            print("Unknown command.")

if __name__ == "__main__":
    main()

# ================= END =================
