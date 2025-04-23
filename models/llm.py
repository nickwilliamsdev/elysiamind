import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

class LLMInterface:
    def respond(self, prompt):
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return completion.choices[0].message["content"].strip()
        except Exception as e:
            return f"(Error generating response: {e})"
