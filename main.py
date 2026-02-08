from app.data_loader import load_shipments
from app.chatbot import chatbot_response

def main():
    print("🚀 Shipping Tracker Chatbot")
    print("Type 'help' for assistance or 'exit' to quit.\n")

    shipments = load_shipments()

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        response = chatbot_response(user_input, shipments)
        print("\nBot:\n" + response + "\n")

if __name__ == "__main__":
    main()
