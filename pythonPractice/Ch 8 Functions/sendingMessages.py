# Write a function called sendMessages() that prints each text message
# and moves each message to a new list called sentMessages as it's printed.
# after calling the function print both lists to make sure the messages
# were moved correctly.
def sendMessages(text_messages, sent_messages):
    """Print a text message."""
    while text_messages:
        current_message = text_messages.pop()
        print(f"Current message: {current_message}")
        sent_messages.append(current_message)

def show_sent_messages(sent_messages):
    """Show all the messages that were sent"""
    print("\nThe following messages have been sent:")
    for sent_message in sent_messages:
        print(sent_message)


messages = ['Good morning!', 'How are you today?', 'Has the dog been fed?']
messages_sent = []

sendMessages(messages[:], messages_sent)
show_sent_messages(messages_sent)

print(f"\nMessages in messages list: {messages}")
print(f"Messages in messages sent list: {messages_sent}")
