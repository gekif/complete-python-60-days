import todo_functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
button = sg.Button("Add")

window = sg.Window(
    'My To-Do App',
layout=[
    [label],
    [input_box, button]
],
    font=('Helvetica', 20)
)

while True:
    event, values = window.read()

    #debug
    print(event)
    print(values)

    match event:
        case "Add":
            todos = todo_functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            todo_functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()