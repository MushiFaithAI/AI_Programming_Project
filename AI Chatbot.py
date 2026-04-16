# Radiant Elegance Chatbot
# Built by Faith Kemuma
# Simple rule-based chatbot for Instagram skincare business
def chatbot():
    print("Bot: Hello! Welcome to Radiant Elegance Skincare. How can I assist you today?")

    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase for easier matching
        
        # Greeting intent
        if "hi" in user_input or "hello" in user_input:
            print("Bot: Hello! Thank you for visiting Radiant Elegance. How can I help you?")
        
        # Location intent
        elif "located" in user_input or "where" in user_input:
            print("Bot: We are based in Nairobi, Kenya. We also deliver nationwide.")
        
        # Products intent
        elif "products" in user_input or "brands" in user_input:
            print("Bot: We offer products from many brands including Biore UV, Nivea, Garnier, CeraVe, L'Oreal Paris, The Ordinary, and many more.")
        
        # Price intent
        elif "price" in user_input or "cost" in user_input:
            print("Bot: Prices vary depending on the brand and product. For example, creams start from KES 1000, serums up to KES 3000.")
        
        # Delivery intent
        elif "deliver" in user_input or "shipping" in user_input:
            print("Bot: Yes, we deliver nationwide. Shipping costs KES 200 per order.")
        
        # Payment intent
        elif "pay" in user_input or "payment" in user_input:
            print("Bot: You can pay via M-Pesa or bank transfer")
        
        # Exit intent
        elif "bye" in user_input or "exit" in user_input:
            print("Bot: Goodbye! Thanks for visiting Radiant Elegance. Have a beautiful day!")
            break
        
        # Default response
        else:
            print("Bot: I'm sorry, I didn't understand that. Can you please rephrase?")

# Run the chatbot
chatbot()