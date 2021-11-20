# Print the file contents 3 ways
# 1 reading in the entire file
# 2 looping over the file object
# 3 storing the lines in a list and then working
# with them outside the with block

filename = 'learning_python.txt'

with open(filename) as f:
    contents = f.read()

print(contents.rstrip())


with open(filename) as f:
    for line in f:
        print(line.rstrip())


with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())