import sys
import google.generativeai as genai
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QScrollArea, QHBoxLayout
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
print(api_key)

api__key = os.getenv("API_KEY")

# Configure the Generative AI with the API key
api_key = api__key  # Add your Google Generative AI API Key here
genai.configure(api_key=api_key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Define the model
model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
)

# Start a chat session
chat_session = model.start_chat(history=[])


class ChatBotApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Chatbot")
        self.setGeometry(100, 100, 600, 600)  # Adjust window size for larger text

        # Chat history area
        self.chat_history = QTextEdit(self)
        self.chat_history.setReadOnly(True)
        self.chat_history.setPlaceholderText("Chatbot: Type 'exit' to quit.")
        self.chat_history.setStyleSheet("font-size: 16px; padding: 10px;")

        # User input field
        self.user_input = QLineEdit(self)
        self.user_input.setPlaceholderText("Type your message...")
        self.user_input.setStyleSheet("font-size: 18px; padding: 10px;")
        self.user_input.returnPressed.connect(self.send_message)

        # Send button
        self.send_button = QPushButton("Send", self)
        self.send_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.send_button.clicked.connect(self.send_message)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.chat_history)
        
        # HBox layout for user input and send button
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.user_input)
        input_layout.addWidget(self.send_button)
        
        layout.addLayout(input_layout)

        container = QWidget()
        container.setLayout(layout)

        # Add scroll area for chat history
        scroll_area = QScrollArea(self)
        scroll_area.setWidget(container)
        scroll_area.setWidgetResizable(True)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

        # Apply dark theme stylesheet
        self.apply_dark_theme()

    def send_message(self):
        user_text = self.user_input.text().strip()  # Remove any surrounding whitespace
        if not user_text:  # If the input is empty after trimming
            return  # Do nothing if input is empty

        if user_text.lower() in ["exit", "bye"]:
            self.chat_history.append("<font size='5' color='#f1f1f1'>Chatbot: 👋 Goodbye!</font>")
            self.user_input.clear()
            return

        # Display user input in chat history (larger text for better visibility)
        self.chat_history.append(f"<font size='4' color='#00BFFF'>You: {user_text}</font>")
        self.user_input.clear()

        # Get response from the model
        response = chat_session.send_message(user_text)
        self.chat_history.append(f"<font size='4' color='#f1f1f1'>Chatbot: {response.text}</font>\n")

        # Scroll to the bottom
        self.chat_history.moveCursor(self.chat_history.textCursor().End)

    def apply_dark_theme(self):
        dark_stylesheet = """
        QWidget {
            background-color: #2e2e2e;
            color: #f1f1f1;
            font-family: Arial, sans-serif;
        }

        QTextEdit {
            background-color: #3c3f41;
            color: #f1f1f1;
            border: 1px solid #444;
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
        }

        QLineEdit {
            background-color: #3c3f41;
            color: #f1f1f1;
            border: 1px solid #444;
            padding: 10px;
            font-size: 18px;
            border-radius: 5px;
        }

        QPushButton {
            background-color: #5c5c5c;
            color: #f1f1f1;
            border: none;
            padding: 10px 20px;
            font-size: 18px;
            border-radius: 5px;
        }

        QPushButton:hover {
            background-color: #888;
        }

        QScrollArea {
            border: none;
        }

        QWidget QScrollBar:vertical {
            background: #444;
            width: 10px;
            border-radius: 5px;
        }

        QWidget QScrollBar::handle:vertical {
            background: #888;
            border-radius: 5px;
        }

        QWidget QScrollBar::handle:vertical:hover {
            background: #aaa;
        }
        """
        self.setStyleSheet(dark_stylesheet)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatBotApp()
    window.show()
    sys.exit(app.exec_())
