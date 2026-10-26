
def chatbot():
    print("\n" + "=" * 42)
    print("           CHATBUDDY")
    print("       A FRIENDLY LITTLE CHAT")
    print("=" * 42)

    print("\nChatBuddy: Hey! Welcome to my little corner.")
    print("ChatBuddy: No special topic needed, just say hello!")
    print("ChatBuddy: Type 'help' for ideas or 'bye' to leave.")

    while True:
        user = input("\nYou: ").lower().strip()

        if user in ["hello", "hi", "hey"]:
            print("ChatBuddy: Hey there! What's on your mind?")

        elif user == "how are you":
            print("ChatBuddy: Pretty good! Thanks for checking in.")
            print("ChatBuddy: I hope you're having a nice day too.")

        elif user in ["i am fine", "i'm fine", "fine"]:
            print("ChatBuddy: That's good to hear! Keep that energy.")

        elif user == "what is your name":
            print("ChatBuddy: I'm ChatBuddy, your tiny chat companion.")

        elif user == "who are you":
            print("ChatBuddy: I'm a little Python program built for a chat!")

        elif user == "help":
            print("\nChatBuddy: Here's our little menu:")
            print("  - Say hello")
            print("  - Ask how I am")
            print("  - Ask my name")
            print("  - Ask for a quote")
            print("  - Ask for a joke")
            print("  - Say thanks or bye")

        elif user in ["thanks", "thank you"]:
            print("ChatBuddy: Anytime! That's what I'm here for.")

        elif user == "good morning":
            print("ChatBuddy: Good morning! Make today count.")

        elif user == "good night":
            print("ChatBuddy: Good night! Tomorrow is a fresh start.")

        elif user == "tell me a joke":
            print("ChatBuddy: Why did the computer go to art class?")
            print("ChatBuddy: It wanted to learn how to draw its own windows!")

        elif user == "quote":
            print("ChatBuddy: Small steps every day lead to big changes.")

        elif user in ["i am sad", "i'm sad"]:
            print("ChatBuddy: Some days are harder than others.")
            print("ChatBuddy: Be kind to yourself. Better moments can come.")

        elif user in ["bye", "goodbye", "exit"]:
            print("\nChatBuddy: Thanks for stopping by!")
            print("ChatBuddy: Until next time, take care.")
            print("=" * 42)
            break

        elif user == "":
            print("ChatBuddy: I'm listening! Type something for me.")

        else:
            print("ChatBuddy: I haven't learned that one yet.")
            print("ChatBuddy: Try 'help' and let's keep chatting.")

chatbot()
