import FreeSimpleGUI as sg

label_compress = sg.Text("Select file to compress:")
input_folder_compress = sg.InputText(tooltip="Folder to compress", key="folder_to_compress")
choose_compress_file = sg.FileBrowse("Browse", key="browse_compress_file")

label_destination_folder = sg.Text("Select destination folder:")
choose_destination_folder = sg.FolderBrowse("Browse", key="browse_destination_folder")
input_destination_folder = sg.InputText(tooltip="Destination folder", key="destination_folder")

compress_button = sg.Button("Compress", key="compress_button")


window = sg.Window('File Compressor', layout=[
    [label_compress, input_folder_compress, choose_compress_file],
    [label_destination_folder, input_destination_folder, choose_destination_folder],
    [compress_button]
])
window.read()
window.close()