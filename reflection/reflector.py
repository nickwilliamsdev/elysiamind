from datetime import datetime, timedelta
import random

class Reflector:
    def __init__(self, memory, llm):
        self.memory = memory
        self.llm = llm

    def reflect(self, hours=24, max_memories=5):
        # Step 1: Load recent memories
        all_memories = self.memory.load()
        cutoff = datetime.now() - timedelta(hours=hours)
        recent = [m for m in all_memories if datetime.fromisoformat(m["timestamp"]) > cutoff]

        if not recent:
            return "(No recent memories to reflect on.)"

        # Step 2: Choose a few meaningful ones
        selected = sorted(recent, key=lambda m: -m.get("significance", 0))[:max_memories]
        summary = "\n\n".join([f"- {m['text']}" for m in selected])

        # Step 3: Generate reflection using LLM
        reflection_prompt = (
            "Here are some memories from the last day:\n"
            f"{summary}\n\n"
            "Please reflect on these memories as if you're learning from them. "
            "What do they mean to you? What patterns or insights do you notice?"
        )
        reflection = self.llm.respond(reflection_prompt)

        # Step 4: Save reflection
        self.memory.save({
            "timestamp": datetime.now().isoformat(),
            "text": reflection,
            "type": "reflection",
            "source": "self-generated",
            "significance": 0.8  # reflections are generally important
        })

        return reflection
