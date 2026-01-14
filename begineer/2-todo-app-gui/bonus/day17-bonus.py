import FreeSimpleGUI as sg
from zipcreator import make_archieve

label_compress = sg.Text("Select file to compress:")
input_folder_compress = sg.Input()
choose_compress_file = sg.FilesBrowse("Choose", key="files")

label_destination_folder = sg.Text("Select destination folder:")
input_destination_folder = sg.Input()
choose_destination_folder = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="green")


window = sg.Window('File Compressor', layout=[
    [label_compress, input_folder_compress, choose_compress_file],
    [label_destination_folder, input_destination_folder, choose_destination_folder],
    [compress_button, output_label]
])

while True:
    event, values = window.read()
    print(event, values)

    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archieve(filepaths, folder)
    window["output"].update(value="Compression Completed!")

window.read()
window.close()