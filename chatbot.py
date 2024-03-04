class ChatBot:
    def __init__(self):
        self.user_data = {}

    def login(self, email):
        if email not in self.user_data:
            self.user_data[email] = []

    def chat(self, email, message):
        if email in self.user_data:
            self.user_data[email].append(message)
        else:
            print("Please login first.")

    def get_chat_history(self, email):
        if email in self.user_data:
            return self.user_data[email]
        else:
            return []

# Example usage:
if __name__ == "__main__":
    bot = ChatBot()

    # User 1 login and chat
    user1_email = "user1@example.com"
    bot.login(user1_email)
    bot.chat(user1_email, "Hello!")
    bot.chat(user1_email, "How are you?")

    # User 2 login and chat
    user2_email = "user2@example.com"
    bot.login(user2_email)
    bot.chat(user2_email, "Hi there!")
    bot.chat(user2_email, "I'm doing well.")

    # Access chat history
    print("User 1's chat history:", bot.get_chat_history(user1_email))
    print("User 2's chat history:", bot.get_chat_history(user2_email))
