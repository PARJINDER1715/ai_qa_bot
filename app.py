import os
from openai import OpenAI

# --- SETUP ---
API_KEY = "OPEN_API_KEY"
client = OpenAI(api_key=API_KEY)

# --- Function to ask question ---
def ask_question(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message["content"]

# --- Console interface ---
if __name__ == "__main__":
    print("🤖 Welcome to AI Q&A Bot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        answer = ask_question(user_input)
        print("AI:", answer)
