import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class PersonalAssistant:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY is missing in the .env file.")
        
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"

    def ask(self, question: str) -> str:
        payload = {
            "model": "llama3-8b-8192",  # Or use another available model
            "messages": [
                {"role": "user", "content": question}
            ],
            "temperature": 0.7
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(self.base_url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()

            # Extract assistant's reply
            return data["choices"][0]["message"]["content"].strip()

        except requests.exceptions.RequestException as e:
            return f"Request failed: {e}"
        except KeyError:
            return "Failed to get a proper response."

def main():
    try:
        assistant = PersonalAssistant()
    except ValueError as e:
        print(e)
        return

    print("Personal Assistant is ready! (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        response = assistant.ask(user_input)
        print(f"Assistant: {response}\n")

if __name__ == "__main__":
    main()
