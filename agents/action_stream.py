import uuid
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from .embedding import get_embedding  # If you're embedding actions
from datetime import datetime, timezone
from .action import TaskAction, CommunicationAction, DecisionAction  # Import the Action subclasses
from annoy import AnnoyIndex  # If you're using approximate nearest neighbor search
from .agent_api_communication import APICommunication  # If actions also communicate with an API


class ActionStream:
    def __init__(self):
        self.id = str(uuid.uuid4())  # Assign a unique ID to the ActionStream instance
        self.nodes = []

    def add_action(self, action):
        self.nodes.append(action)

    def get_action_by_id(self, action_id):
        for action in self.nodes:
            if action.id == action_id:
                return action
        return None

    def delete_action(self, action_id):
        self.nodes = [node for node in self.nodes if node.id != action_id]

    def search_action(self, query):
        pass
