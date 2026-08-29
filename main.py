# Simple Rule-Based Chatbot 🤖

def chatbot():
    print("Chatbot: Hello! Type 'exit' to quit.")
    
    while True:  # Continuous loop
        user_input = input("You: ").lower()
        
        # Handle exit
        if user_input == "exit":
            print("Chatbot: Goodbye! Have a nice day.")
            break
        
        # Handle greetings
        elif user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hi there! How can I help you?")
        
        # Handle thanks
        elif user_input in ["thanks", "thank you"]:
            print("Chatbot: You're welcome!")
        
        # Handle custom responses
        elif user_input in ["how are you", "how r u"]:
            print("Chatbot: I'm just a bot, but I'm doing great!")
        
        else:
            print("Chatbot: Sorry, I don't understand that.")
            

# Run chatbot
chatbot()
