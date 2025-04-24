import os
import json
from datetime import datetime

MEMORY_FILE = "memory/memories.jsonl"

def ensure_memory_file_exists():
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    if not os.path.isfile(MEMORY_FILE):
        with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
            pass  # Create an empty file

def save_memory(memory):
    ensure_memory_file_exists()
    with open(MEMORY_FILE, 'a', encoding='utf-8') as f:
        json.dump(memory, f)
        f.write('\n')

def load_memories():
    ensure_memory_file_exists()
    with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f if line.strip()]

def find_memories_by_tag(tag):
    return [m for m in load_memories() if m.get("tag") == tag]

def find_recent_memories(n=5):
    return load_memories()[-n:]

def clear_all_memories():
    open(MEMORY_FILE, 'w').close()
