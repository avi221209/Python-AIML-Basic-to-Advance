def chatbot(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you?"
    elif "name" in message:
        return "I am an AI chatbot."
    elif "bye" in message:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Chat ended")
        break
    print("Bot:", chatbot(user_input))
