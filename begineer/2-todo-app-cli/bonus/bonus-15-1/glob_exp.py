import glob

myfiles = glob.glob("files/*.txt")

for file in myfiles:
    with open(file, 'r') as f:
        content = f.read()
        print(f"Contents of {file}:\n{content}\n")