import sys

# Ensure the terminal handles UTF-8 emojis on Windows without crashing
try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if hasattr(sys.stdin, 'reconfigure'):
        sys.stdin.reconfigure(encoding='utf-8')
except Exception:
    pass

def safe_print(message):
    """Prints message safely, falling back to ASCII if Unicode encoding fails."""
    try:
        print(message)
    except UnicodeEncodeError:
        # Fallback by removing emojis or non-ASCII characters
        clean_msg = message.encode('ascii', 'ignore').decode('ascii')
        print(clean_msg)

safe_print("🤖 Chatbot: Hello! Type 'exit' to end the chat.")

while True:
    try:
        # Added .strip() to solve match errors caused by trailing/leading spaces
        user = input("You: ").strip().lower()
    except (KeyboardInterrupt, EOFError):
        print() # Move to a new line after Ctrl+C / Ctrl+D
        safe_print("🤖 Chatbot: Goodbye! Have a nice day.")
        break

    # Skip empty inputs instead of printing "I don't understand"
    if not user:
        continue

    # Decision-making logic using if-elif-else (control flow)
    if user in ("hello", "hi", "hey"):
        safe_print("🤖 Chatbot: Hello! How can I help you?")
    elif user == "how are you":
        safe_print("🤖 Chatbot: I'm doing great! Thanks for asking.")
    elif user == "what is your name":
        safe_print("🤖 Chatbot: My name is RuleBot.")
    elif user in ("bye", "exit", "quit"):
        safe_print("🤖 Chatbot: Goodbye! Have a nice day.")
        break
    else:
        safe_print("🤖 Chatbot: Sorry, I don't understand that.")
