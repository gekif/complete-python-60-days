import FreeSimpleGUI as sg

label_feet = sg.Text("Enter feet:")
input_feet = sg.InputText(tooltip="Feet")

label_inches = sg.Text("Enter inches:")
input_inches = sg.InputText(tooltip="Inches")

button_convert = sg.Button("Convert")

window = sg.Window('Converter', layout=[
    [label_feet, input_feet],
    [label_inches, input_inches],
    [button_convert]
])
window.read()
window.close()