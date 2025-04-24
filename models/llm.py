import requests

class LLMInterface:
    def __init__(self, model_name="llama2"):
        self.model_name = model_name
        self.api_url = "http://localhost:11434/api/generate"

    def respond(self, prompt):
        try:
            response = requests.post(self.api_url, json={
                "model": self.model_name,
                "prompt": prompt,
                "stream": False
            })

            if response.status_code == 200:
                return response.json().get("response", "").strip()
            else:
                return f"(Error: {response.status_code} - {response.text})"

        except Exception as e:
            return f"(Error generating response: {e})"
