import todo_functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=todo_functions.get_todos(), key="todos", enable_events=True, size=(45, 10))

# button_labels = ["Close", "Apply"]

# layout = []

# for bl in button_labels:
#     layout.append([sg.Button(bl)])

layout = [
    [label],
    [input_box, add_button],
    [list_box, edit_button]
    # [bl[0] for bl in layout]
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


        case "todos":
            window['todo'].update(values['todos'][0])


        case sg.WIN_CLOSED:
            break

window.close()