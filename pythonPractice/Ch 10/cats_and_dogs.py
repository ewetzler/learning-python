def read_names(filename):
    """Read the names of words in a file."""
    try:
        with open(filename, 'r') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    read_names(filename)