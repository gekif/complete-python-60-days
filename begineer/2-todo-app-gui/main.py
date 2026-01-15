import todo_functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
# add_button = sg.Button("Add")
# edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=todo_functions.get_todos(), key="todos", enable_events=True, size=(45,10))

button_labels = ["Add", "Edit", "Complete", "Delete", "Exit"]

layout = []

for bl in button_labels:
    layout.append([sg.Button(bl)])

layout = [
    [label],
    [input_box],
    [list_box],
    [bl[0] for bl in layout]
]

window = sg.Window(
    'My To-Do App',
    layout=layout,
    font=('Helvetica', 20)
)

while True:
    event, values = window.read()

    #debug
    print(event)
    print(values)
    print(values['todos'])

    match event:
        case "Add":
            todos = todo_functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            todo_functions.write_todos(todos)

            # 🔥 UPDATE LISTBOX
            window['todos'].update(values=todos)
            window['todo'].update('')


        case "Edit":
            todos = todo_functions.get_todos()
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            todo_functions.write_todos(todos)

            # 🔥 UPDATE LISTBOX
            window['todos'].update(values=todos)
            window['todo'].update('')

        case "Complete":
            todos = todo_functions.get_todos()
            todo_to_complete = values['todos'][0]
            todos.remove(todo_to_complete)
            todo_functions.write_todos(todos)
            todo_functions.append_completed(todo_to_complete)

            # 🔥 UPDATE LISTBOX
            window['todos'].update(values=todos)
            window['todo'].update('')

        case "Delete":
            todos = todo_functions.get_todos()
            todo_to_delete = values['todos'][0]
            todos.remove(todo_to_delete)
            todo_functions.write_todos(todos)

            # 🔥 UPDATE LISTBOX
            window['todos'].update(values=todos)
            window['todo'].update('')

        case "Exit":
            break


        case "todos":
            window['todo'].update(values['todos'][0])


        case sg.WIN_CLOSED:
            break

window.close()