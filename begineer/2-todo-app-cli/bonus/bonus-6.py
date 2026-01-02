contents = [
    "All carrots are "
    "eaten by.",
    "The carrots reportedly sliced.",
    "Arrivederci"
]

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)