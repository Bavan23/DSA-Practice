import google.generativeai as genai

api_key = ""

genai.configure(api_key=api_key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
)

chat_session = model.start_chat(history=[])

print("\n🤖 AI Chatbot: Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    exit=["exit","bye"]
    if user_input.lower() in exit:
        print("Chatbot: 👋 Goodbye!")
        break
    
    response = chat_session.send_message(user_input)
    print(f"Chatbot: {response.text}\n")
