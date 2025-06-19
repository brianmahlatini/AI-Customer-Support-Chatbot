"""
AI-Powered Customer Support Chatbot
Author: Brian Mahlatini
Experience Level: 3+ years (Mid-level NLP & Automation)
Description:
  - Intent recognition using spaCy NLP
  - Modular, clean code structure
  - Detailed logging of conversation
  - Multiple intents & fallback response
  - CLI chat interface
  - Easily extendable for future AI/GPT integration
"""

import spacy
import logging
from datetime import datetime

# Initialize logger
logging.basicConfig(
    filename="chatbot_session.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Load spaCy English model (make sure to run: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

# Define chatbot intents with keywords and responses
INTENTS = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "morning", "evening"],
        "response": "Hello! How can I assist you today?"
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you", "farewell"],
        "response": "Goodbye! Have a great day."
    },
    "thanks": {
        "keywords": ["thanks", "thank you", "appreciate"],
        "response": "You're most welcome."
    },
    "billing": {
        "keywords": ["payment", "bill", "charge", "invoice"],
        "response": "Billing issues are common. Would you like to speak to a billing agent?"
    },
    "support": {
        "keywords": ["problem", "issue", "error", "help", "support"],
        "response": "Please provide more details so I can assist you better."
    },
    "food": {
        "keywords": ["hungry", "eat", "food", "meal"],
        "response": "If you're hungry, how about ordering some food or trying a quick recipe?"
    },
    "general_question": {
        "keywords": ["what", "how", "why", "where", "when"],
        "response": "That’s an interesting question! Could you please clarify or provide more details?"
    },
    # Fallback intent for unknown inputs
    "unknown": {
        "response": "I'm not sure I understand. I’ll escalate this to a human support agent."
    }
}

def log_interaction(role, message):
    """
    Logs conversation messages with timestamps.
    :param role: 'User' or 'Chatbot'
    :param message: message text
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {role}: {message}"
    print(log_message)  # Also print on console
    logging.info(log_message)

def detect_intent(message):
    """
    Detect intent of the message using spaCy and keyword matching.
    :param message: user input string
    :return: intent key
    """
    doc = nlp(message.lower())
    for intent, data in INTENTS.items():
        if intent == "unknown":
            continue  # Skip fallback for now
        for token in doc:
            if token.lemma_ in data["keywords"]:
                return intent
    return "unknown"

def get_response(intent):
    """
    Get chatbot response based on intent.
    :param intent: intent key
    :return: response string
    """
    return INTENTS[intent]["response"]

def run_chatbot():
    """
    Runs the chatbot command line interface.
    """
    print("\n🤖 AI-Powered Customer Support Chatbot")
    print("Type your message and press Enter. Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("🧑 You: ").strip()
        if not user_input:
            continue  # Ignore empty input
        log_interaction("User", user_input)

        if user_input.lower() in ("exit", "quit"):
            farewell_msg = "Session ended. Thank you for chatting!"
            log_interaction("Chatbot", farewell_msg)
            print(f"\n🤖 Chatbot: {farewell_msg}")
            break

        intent = detect_intent(user_input)
        response = get_response(intent)
        log_interaction("Chatbot", response)
        print(f"\n🤖 Chatbot: {response}\n")

if __name__ == "__main__":
    run_chatbot()
