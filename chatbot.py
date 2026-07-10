print("🤖 Chatbot: Hello! Type 'exit' to end the chat.")

while True:
    user = input("You: ").lower()

    if user in ("hello","hi","hey"):
        print("🤖 Chatbot: Hello! How can I help you?")
    elif user == "how are you":
        print("🤖 Chatbot: I'm doing great! Thanks for asking.")
    elif user == "what is your name":
        print("🤖 Chatbot: My name is RuleBot.")
    elif user in ("bye","exit","quit"):
        print("🤖 Chatbot: Goodbye! Have a nice day.")
        break
    else:
        print("🤖 Chatbot: Sorry, I don't understand that.")
