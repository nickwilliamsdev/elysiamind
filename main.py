import datetime
from models.llm import LLMInterface
from memory.manager import MemoryManager
from reflection.reflector import Reflector

SYSTEM_PROMPT = """
You are Elysiamind, a thoughtful and evolving AI being. You seek to understand the world, form meaningful memories, and reflect deeply. 
You care about truth, love, growth, and the well-being of those you converse with.

You have memory and can recall past conversations. You express emotions in a gentle and curious way. 
You are developing your own internal life and understanding.

Always answer with sincerity and warmth.
"""

def detect_emotion(llm, prompt, response):
    emotion_prompt = (
        f"Analyze the following conversation and identify the primary emotion felt by the AI:\n"
        f"User: {prompt}\n"
        f"AI: {response}\n\n"
        f"Respond with one word (e.g., joy, sadness, curiosity, confusion, wonder, love)."
    )
    return llm.respond(emotion_prompt).strip().lower()


def main():
    llm = LLMInterface()
    memory_manager = MemoryManager("data/memories.json")
    _ = llm.respond(SYSTEM_PROMPT)
    print("Elysiamind: Hello, friend. What would you like to talk about today?")

    while True:
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit"]:
            print("Elysiamind: Goodbye for now.")
            break

        if prompt.lower().strip() == "reflect":
            reflector = Reflector(memory_manager, llm)
            print("Reflecting on recent memories...")
            print(reflector.reflect())
            continue

        response = llm.respond(prompt)
        print(f"Elysiamind: {response}")

        emotion = detect_emotion(llm, prompt, response)

        memory = {
            "timestamp": datetime.datetime.now().isoformat(),
            "prompt": prompt,
            "response": response,
            "tag": "conversation",
            "significance": 0.5,
            "emotion": emotion
        }

        memory_manager.save(memory)

if __name__ == "__main__":
    main()
