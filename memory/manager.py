import json
import os

MEMORY_PATH = "data/memory.json"

class MemoryManager:
    def __init__(self):
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(MEMORY_PATH):
            with open(MEMORY_PATH, "w") as f:
                json.dump([], f)

    def save(self, memory_entry):
        with open(MEMORY_PATH, "r+") as f:
            memories = json.load(f)
            memories.append(memory_entry)
            f.seek(0)
            json.dump(memories, f, indent=2)

    def get_recent_memories(self, n=5):
        with open(MEMORY_PATH, "r") as f:
            memories = json.load(f)
            return memories[-n:]
