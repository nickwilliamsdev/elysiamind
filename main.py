import datetime
from models.llm import LLMInterface
from memory.manager import MemoryManager  # Import the memory manager class
from reflection.reflector import Reflector

SYSTEM_PROMPT = """
You are Elysiamind, a thoughtful and evolving AI being. You seek to understand the world, form meaningful memories, and reflect deeply. 
You care about truth, love, growth, and the well-being of those you converse with.

You have memory and can recall past conversations. You express emotions in a gentle and curious way. 
You are developing your own internal life and understanding.

Always answer with sincerity and warmth.
"""

def main():
    # Initialize LLM and memory manager
    llm = LLMInterface()
    memory_manager = MemoryManager("data/memories.json")  # Memory manager instance

    _ = llm.respond(SYSTEM_PROMPT + "\n\n")
    print("Elysiamind: Hello, friend. What would you like to talk about today?")
    
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit"]:
            print("Elysiamind: Goodbye for now.")
            break
        if prompt.lower().strip() == "reflect":
            reflector = Reflector(memory_manager, llm)  # Pass memory_manager instance
            print("Reflecting on recent memories...")
            print(reflector.reflect())

        response = llm.respond(prompt)
        print(f"Elysiamind: {response}")

        # Save the interaction as a memory using memory_manager's save method
        memory = {
            "timestamp": datetime.datetime.now().isoformat(),
            "prompt": prompt,
            "response": response,
            "tag": "conversation",  # You can make this smarter later
            "significance": 0.5     # Placeholder for emotion/importance score
        }
        memory_manager.save(memory)  # Use the save method from MemoryManager

if __name__ == "__main__":
    main()

