"""
Simple Chatbot with Keyword Matching
A conversational agent that responds to user inputs based on predefined keywords.
"""

import random
from datetime import datetime


class SimpleChatbot:
    """A simple rule-based chatbot using keyword matching."""
    
    def __init__(self, name="PyBot"):
        """Initialize the chatbot with a name and response dictionary."""
        self.bot_name = name
        self.conversation_log = []
        
        # Dictionary of keyword-response pairs (keywords mapped to response lists)
        self.responses = {
            "hello": [
                "Hello! How are you doing today?",
                "Hi there! Nice to meet you!",
                "Hey! How can I help you?"
            ],
            "hi": [
                "Hi! What's on your mind?",
                "Hello! Good to see you!",
                "Hey there! How's it going?"
            ],
            "how are you": [
                "I'm doing great, thanks for asking! How about you?",
                "I'm functioning perfectly! How are you?",
                "All systems running smoothly here! What about you?"
            ],
            "what is your name": [
                f"I'm {self.bot_name}, your friendly chatbot!",
                f"My name is {self.bot_name}. What's yours?",
                f"You can call me {self.bot_name}!"
            ],
            "help": [
                "I'm here to chat! You can ask me how I'm doing, tell me about yourself, or just say 'bye' to exit.",
                "I can have a conversation with you! Try saying hello, asking how I am, or typing 'bye' to leave.",
                "Feel free to chat with me about anything. Type 'bye' when you're done!"
            ],
            "thanks": [
                "You're welcome!",
                "Happy to help!",
                "Anytime! Is there anything else?"
            ],
            "thank you": [
                "You're very welcome!",
                "My pleasure!",
                "Glad I could assist!"
            ],
            "what time is it": [
                f"The current time is {datetime.now().strftime('%I:%M %p')}",
                f"It's {datetime.now().strftime('%H:%M')} right now.",
                f"The time is {datetime.now().strftime('%I:%M %p')}"
            ],
            "what's the weather": [
                "I don't have access to weather data, but you can check a weather website!",
                "Sorry, I can't check weather. Try a weather app!",
                "I wish I could help with weather, but that's outside my abilities!"
            ],
            "who are you": [
                f"I'm {self.bot_name}, an AI chatbot designed to chat with you!",
                f"I'm {self.bot_name}, here to keep you company!",
                "I'm a friendly chatbot ready to talk!"
            ],
            "bye": [
                "Goodbye! It was nice chatting with you!",
                "See you later! Have a great day!",
                "Bye! Thanks for the conversation!",
                "Take care! Come back soon!"
            ]
        }
        
        # Default responses for unmatched inputs
        self.default_responses = [
            "That's interesting! Tell me more.",
            "I see. How does that make you feel?",
            "I didn't quite understand that. Can you rephrase?",
            "That's cool! Anything else on your mind?",
            "Hmm, I'm still learning. Can you explain further?",
            "Interesting thought! What else is there?"
        ]
    
    def find_response(self, user_input):
        """
        Find an appropriate response based on user input keywords.
        
        Args:
            user_input (str): The user's message
            
        Returns:
            str: A response from the chatbot
        """
        user_input_lower = user_input.lower().strip()
        
        # Check for exact keyword matches first
        for keyword, response_list in self.responses.items():
            if keyword in user_input_lower:
                return random.choice(response_list)
        
        # Return a random default response if no keyword matched
        return random.choice(self.default_responses)
    
    def greet(self):
        """Display a greeting message."""
        greeting = f"Hi! I'm {self.bot_name}. Type 'help' for a list of things I can assist with, or just start chatting!"
        print(f"\n{self.bot_name}: {greeting}\n")
    
    def chat(self):
        """Start the conversation loop."""
        self.greet()
        
        while True:
            try:
                # Capture user input
                user_input = input("You: ").strip()
                
                # Skip empty inputs
                if not user_input:
                    print(f"{self.bot_name}: Please say something!\n")
                    continue
                
                # Log the conversation
                self.conversation_log.append(("User", user_input))
                
                # Get and display the response
                response = self.find_response(user_input)
                print(f"{self.bot_name}: {response}\n")
                self.conversation_log.append((self.bot_name, response))
                
                # Check if user wants to exit
                if "bye" in user_input.lower():
                    break
                    
            except KeyboardInterrupt:
                print(f"\n{self.bot_name}: Interrupted. Goodbye!\n")
                break
            except Exception as e:
                print(f"{self.bot_name}: An error occurred: {e}. Let's continue!\n")
    
    def print_conversation_log(self):
        """Print the conversation history."""
        print("\n--- Conversation Log ---")
        for speaker, message in self.conversation_log:
            print(f"{speaker}: {message}")
        print("------------------------\n")


def main():
    """Main function to run the chatbot."""
    chatbot = SimpleChatbot(name="PyBot")
    chatbot.chat()
    # Optionally print conversation log
    chatbot.print_conversation_log()


if __name__ == "__main__":
    main()
