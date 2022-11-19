from chatbot import related, send_message

print("Hey!! May I know your name please")
user_name = input()

# Creating template
print("Bot : Hey", user_name)

while True:
    my_input = input("{} : ".format(user_name))
    my_input = my_input.lower()
    related_text = related(my_input)
    if my_input == "exit" or my_input == "bye":
        print('Take care, have a nice day!')
        break
    send_message(related_text)
