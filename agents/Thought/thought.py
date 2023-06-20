import uuid
from ..embedding import get_embedding
from datetime import timezone, datetime
from ..convert_timestamp import convert_to_utc_timestamp

class Thought:
    count = 0

    def __init__(self, thought_type, content, timestamp):
        self.id = str(uuid.uuid4())
        self.number = Thought.count
        Thought.count += 1

        self.type = thought_type
        self.content = content
        self.timestamp = timestamp
        self.embedding = get_embedding(content)
        self.symbol = "💭"
        self.last_viewed = None

    def update_last_viewed(self, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now(timezone.utc)
        self.last_viewed = timestamp

class Reflection(Thought):
    def __init__(self, content, timestamp, importance, evidence):
        super().__init__("reflection", content, timestamp)
        self.importance = importance
        self.evidence = evidence  
        self.symbol = "💭🪞"

def generate_reflection(memory_stream, content, timestamp, importance, evidence_ids):
    evidence = []
    for memory_id in evidence_ids:
        memory = memory_stream.get_memory_by_id(memory_id)
        if memory is not None:
            evidence.append(memory)  # Add the memory object instead of its content
    reflection = Reflection(content=content, timestamp=timestamp, importance=importance, evidence=evidence)
    memory_stream.add_memory(reflection)
    return reflection

