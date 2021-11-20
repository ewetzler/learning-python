# Make a list  containing a series of short text messages.
# Pass the list to a function that prints each text message.
def showMessages(textMessages):
    """Print a text message."""
    for textMessage in textMessages:
        print(textMessage)


messages  = ['Good morning!', 'How are you today?', 'Has the dog been fed?']
showMessages(messages)