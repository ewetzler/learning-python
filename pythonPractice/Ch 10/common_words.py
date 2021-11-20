def count_words(filename, searchword):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.lower().count(searchword)
        print(f"The file {filename} has about {words}.")

filenames = ['text_files/pride_and_prejudice.txt', 'text_files/sherlock_holmes.txt', 'text_files/the_scarlet_letter.txt']
searchword = 'the '
for filename in filenames:
    count_words(filename, searchword)
