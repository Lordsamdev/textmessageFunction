sms = ["I love you.", "Call me.", "I am in a meeting.", "I'll be with you soon.", "Can't talk Now."]
inbox = []


# def show_message(message):
# for txt in message:
# print(f"\n {txt}")

# show_message(sms)

def send_messages(message, sent_messages): # Parameters are both lists
    while message:  # Iterating through the first list
        msg = message.pop()
        sent_messages.append(msg)  # Transferring messages to sent_messages
    for txt in sent_messages:
        print(f"\n... Sending... {txt}!")  # Printing The sent messages



send_messages(sms[:], inbox)
print(inbox)
print(sms)