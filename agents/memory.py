import uuid
from .embedding import get_embedding
from datetime import timezone, datetime
from .convert_timestamp import convert_to_utc_timestamp

class Memory:

    count = 0

    def __init__(self, memory_type, content, importance, timestamp):
        self.id = str(uuid.uuid4())
        self.number = Memory.count
        Memory.count += 1

        self.type = memory_type
        self.content = content
        self.importance = importance
        self.timestamp = timestamp  
        self.last_viewed = None
        self.embedding = get_embedding(content)
        self.symbol = "🧠"
    
    def update_last_viewed(self, timestamp):
        self.last_viewed = timestamp

class Observation(Memory):
    def __init__(self, content, timestamp, importance):
        timestamp_dt = convert_to_utc_timestamp(timestamp)
        super(Observation, self).__init__("observation", content, importance, timestamp_dt)
        self.symbol = "🧠🧐"
       

class Plan(Memory):
    def __init__(self, content, timestamp, importance, level=None):
        timestamp_dt = convert_to_utc_timestamp(timestamp)
        super(Plan, self).__init__("plan", content, importance, timestamp_dt)
        self.symbol = "🧠🗓️ "
        self.level = level

        def __str__(self):
            return f"Plan(content='{self.content}', timestamp={self.timestamp}, importance={self.importance}, level='{self.level}')"

class Ideal(Memory):
    def __init__(self, content, timestamp, importance):
        timestamp_dt = convert_to_utc_timestamp(timestamp)
        super(Ideal, self).__init__("ideal", content, importance, timestamp_dt)
        self.symbol = "🧠💡"

class Reflection(Memory):
    def __init__(self, content, importance, timestamp, evidence):
        timestamp_dt = convert_to_utc_timestamp(timestamp)
        super(Reflection, self).__init__("reflection", content, importance, timestamp_dt)
        self.symbol = "🧠🪞"
        self.evidence = evidence

        