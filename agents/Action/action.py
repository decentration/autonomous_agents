import uuid
from datetime import timezone, datetime
from ..convert_timestamp import convert_to_utc_timestamp  

class Action:
    def __init__(self, action_type, content, timestamp, associated_task):
        self.id = str(uuid.uuid4())
        self.type = action_type
        self.content = content
        self.timestamp = timestamp
        self.associated_task = associated_task
        self.symbol = "🎬"

    def execute(self):
        raise NotImplementedError

class Strategic(Action):
    def __init__(self, content, timestamp, associated_task, strategy):
        super().__init__("strategic", content, timestamp, associated_task)
        self.strategy = strategy  # the strategic plan this action is part of

class Operational(Action):
    def __init__(self, content, timestamp, associated_task, operations):
        super().__init__("operational", content, timestamp, associated_task)
        self.operations = operations  # the operations this action is part of

class Management(Action):
    def __init__(self, content, timestamp, associated_task, management):
        super().__init__("management", content, timestamp, associated_task)
        self.management = management  # the management team or person this action is related to

class Communication(Action):
    def __init__(self, content, timestamp, associated_task, communication):
        super().__init__("communication", content, timestamp, associated_task)
        self.communication = communication  # the communication strategy this action is part of

class Development(Action):
    def __init__(self, content, timestamp, associated_task, development):
        super().__init__("development", content, timestamp, associated_task)
        self.development = development  # the development plan this action is part of
