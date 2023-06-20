import uuid
from datetime import timezone, datetime
from ..convert_timestamp import convert_to_utc_timestamp

class ThoughtStream:
    def __init__(self):
        self.thoughts = []

    def add_thought(self, thought):
        self.thoughts.append(thought)

    def get_thought_by_id(self, thought_id):
        for thought in self.thoughts:
            if thought.id == thought_id:
                return thought
        return None

    def get_thoughts_by_type(self, thought_type):
        return [thought for thought in self.thoughts if thought.type == thought_type]

    def get_latest_thoughts(self, limit=10):
        return self.thoughts[-limit:]
