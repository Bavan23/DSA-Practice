    user_text = self.user_input.text().strip()  # Remove any surrounding whitespace
        if not user_text:  # If the input is empty after trimming
            return  # Do nothing if input is empty

        if user_text.lower() in ["exit", "bye"]:
            self.chat_history.append("Chatbot: 👋 Goodbye!")
            self.user_input.clear()
            return

        # Display user input in chat history
        self.chat_history.append(f"You: {user_text}")
        self.user_input.clear()

        # Get response from the model
        response = chat_session.send_message(user_text)
        self.chat_history.append(f"Chatbot: {response.text}\n")

        # Scroll to the bottom
        self.chat_history.moveCursor(self.chat_history.textCursor().End)
