import random

#Responses
responses = {
    "hello": [
        "Hi there!",
        "hello!",
        "Hey",
        "Hey there!",
        "Hi! How's it going?",
        "Good day! How may I assist you?",
        "Hello! Hope you're having a great day!",
        "Well, hello there!",
        "Hi! It's nice to hear from you.",
        "Hey! What's new with you?",
        "Hello! What's on your mind today?",
        "Hi!",
        "Hello! What can I do for you?"
    ],

    "hi": [
        "Hi there!",
        "hello!",
        "Hey",
        "Hey there!",
        "Hi! How's it going?",
        "Good day! How may I assist you?",
        "Hello! Hope you're having a great day!",
        "Well, hello there!",
        "Hi! It's nice to hear from you.",
        "Hey! What's new with you?",
        "Hello! What's on your mind today?",
        "Hi!",
        "Hello! What can I do for you?"
    ],

    "hey": [
        "Hi there!",
        "hello!",
        "Hey",
        "Hey there!",
        "Hi! How's it going?",
        "Good day! How may I assist you?",
        "Hello! Hope you're having a great day!",
        "Well, hello there!",
        "Hi! It's nice to hear from you.",
        "Hey! What's new with you?",
        "Hello! What's on your mind today?",
        "Hi!",
        "Hello! What can I do for you?"
    ],

    "how are you": [
        "I'm just a Bot, But I'm doing Fine.",
        "I don't have feelings, but I'm here to help!",
        "I'm just a bunch of code, but thanks for asking! How about you?",
        "Doing great, thanks! How are you?",
        "I’m here and ready to help! How can I assist you today?",
        "I'm doing well! How's everything on your end?",
        "I'm good! What about you?",
        "Feeling chatty as always! What's up with you?",
        "I'm here to help, so let's get started! How are you?",
        "I'm doing well, thanks! How can I make your day better?"
    ],
    "bye": [
        "Goodbye!",
        "See you later!",
        "Bye bye!",
        "Goodbye! Have a great day ahead!",
        "See you later! Take care!",
        "Bye! Feel free to reach out anytime!",
        "Take care! Until next time!",
        "Farewell! It was nice chatting with you!",
        "Goodbye! Stay safe and see you soon!"
    ],
    "default": [
        "I'm not sure how to respond to that!",
        "Could you please rephrase the sentences!",
        "I'm still in learning phase!",
        "I'm sorry, I didn't understand that. Can you please rephrase?",
        "Oops! That didn't quite make sense. Could you try again?",
        "I'm not sure how to respond to that. Could you clarify?",
        "Hmm, I don't have an answer for that. Can you ask something else?",
        "Sorry, I didn't get that. Mind saying it another way?",
        "I didn't catch that. Could you give me more details?"
    ]
}

#function to get response
def get_response(message):
    message = message.lower()
    if message in responses:
        return random.choice(responses[message])
    
    else:
        return random.choice(responses["default"])

#Mainloop Program
print("Chatbot: hi there! How can i assist? (type 'bye' to exit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break

    response = get_response(user_input)

    print(response)