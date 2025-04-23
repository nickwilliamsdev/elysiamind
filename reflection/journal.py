import json
import os
import openai

REFLECTION_PATH = "data/reflections.json"

class Journal:
    def __init__(self):
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(REFLECTION_PATH):
            with open(REFLECTION_PATH, "w") as f:
                json.dump([], f)

    def reflect(self, memories):
        summary_prompt = "Based on these memories, write a short reflection about what I’ve learned, felt, and how I’m growing:\n\n"
        for m in memories:
            summary_prompt += f"- User: {m['user_input']}\n"
            summary_prompt += f"  AI: {m['ai_response']} (emotion: {m['emotion']})\n"

        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": summary_prompt}]
            )
            reflection = completion.choices[0].message["content"].strip()
            self._save(reflection)
            return reflection
        except Exception as e:
            return f"(Error generating reflection: {e})"

    def _save(self, reflection):
        with open(REFLECTION_PATH, "r+") as f:
            data = json.load(f)
            data.append({"text": reflection})
            f.seek(0)
            json.dump(data, f, indent=2)
