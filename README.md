# AI-Customer-Support-Chatbot
AI-powered chatbot with intent detection using spaCy, Python CLI interface, and logging
AI-Powered Customer Support Chatbot

Overview
This project is a command-line chatbot designed to simulate a customer support assistant using natural language processing (NLP). Built with Python and spaCy, the chatbot recognizes user intents and responds accordingly, providing helpful replies for common queries such as greetings, billing issues, support requests, and more.
The chatbot demonstrates key software development skills including:
•	NLP intent detection with spaCy
•	Modular, maintainable code structure
•	Detailed logging of conversations with timestamps
•	Handling multiple intents and fallback responses
•	Clean and user-friendly command-line interface
This project showcases a mid-level developer's capabilities (3+ years experience) in AI, automation, and software engineering best practices.

Features
•	Intent Recognition: Detects user intents via spaCy’s linguistic processing and keyword matching
•	Multiple Intents: Supports greetings, billing, support, thanks, food-related queries, general questions, and unknown fallback
•	Logging: Logs all user and chatbot messages with timestamps to a log file for traceability
•	Command-Line Interface: Simple and interactive text-based chat interface
•	Expandable: Easily extendable to integrate more advanced AI models or web interfaces

Requirements
•	Python 3.7 or higher
•	spaCy NLP library
•	spaCy English language model en_core_web_sm

Installation
1.	Clone the repository or download the script file.
2.	Install dependencies by running these commands in your terminal or Anaconda Prompt:
nginx
CopyEdit
pip install spacy
python -m spacy download en_core_web_sm

Usage
Run the chatbot script in your terminal or IDE:
nginx
CopyEdit
python ai_chatbot.py
Start chatting! Type messages and press Enter.
Type exit or quit to end the session.

Example Conversation
yaml
CopyEdit
🤖 AI-Powered Customer Support Chatbot
Type your message and press Enter. Type 'exit' or 'quit' to stop.

🧑 You: Hello
🤖 Chatbot: Hello! How can I assist you today?

🧑 You: I have a billing issue
🤖 Chatbot: Billing issues are common. Would you like to speak to a billing agent?

🧑 You: Thanks
🤖 Chatbot: You're most welcome.

🧑 You: exit
🤖 Chatbot: Session ended. Thank you for chatting!

Future Improvements
•	Integrate with GPT-based models for more natural conversations
•	Develop a web-based UI using frameworks like Gradio or Flask
•	Add multi-turn dialogue management to maintain context
•	Implement unit and integration tests

Author
Brian Mahlatini
www.linkedin.com/in/brianmahlatini

mahlatinibrian@gmail.com


License
This project is open-source and free to use under the MIT License.

