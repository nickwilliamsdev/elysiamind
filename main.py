from memory.manager import MemoryManager
from emotions.tagger import EmotionTagger
from models.llm import LLMInterface
from reflection.journal import Journal
import datetime

def main():
    llm = LLMInterface()
    memory = MemoryManager()
    emotions = EmotionTagger()
    journal = Journal()

    print("Elysiamind v0.1 — Type 'reflect' to view journal or 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        elif user_input.lower() == "reflect":
            reflection = journal.reflect(memory.get_recent_memories(5))
            print("\nReflection:\n", reflection, "\n")
            continue

        emotion = emotions.tag(user_input)
        response = llm.respond(user_input)
        
        memory.save({
            "timestamp": datetime.datetime.now().isoformat(),
            "user_input": user_input,
            "ai_response": response,
            "emotion": emotion,
            "significance": emotions.significance_score(emotion)
        })

        print("Elysiamind:", response)

if __name__ == "__main__":
    main()
