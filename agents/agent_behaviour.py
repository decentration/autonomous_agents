from agents.autonomous_agent import AutonomousAgent
from agents.Memory.memory import MemoryStream, ReflectionTree, TreeNode
from .utils import calculate_importance_sum, generate_reflection

class AgentBehavior:
    def __init__(self, agent):
        self.agent = agent
        self.memory_stream = MemoryStream()
        self.reflection_tree = ReflectionTree()

    def add_memory(self, memory):
        self.memory_stream.add_memory(memory)

    def check_importance_and_generate_reflection(self, n_latest_events=5, importance_threshold=20):
        importance_sum = calculate_importance_sum(self.memory_stream.memories, n_latest_events)
        if importance_sum >= importance_threshold:
            reflection = generate_reflection(self.memory_stream.memories)
            self.memory_stream.add_memory(reflection)

            reflection_node = TreeNode(reflection)
            for evidence_idx in reflection.evidence:
                self.reflection_tree.children[evidence_idx].add_child(reflection_node)

    # Add other necessary methods for agent behavior management here
agent = AutonomousAgent()
agent_behavior = AgentBehavior(agent)

# Add a new memory item to the memory_stream
new_memory_item = ...
agent_behavior.add_memory(new_memory_item)

# Check the importance and generate a reflection if needed
agent_behavior.check_importance_and_generate_reflection()
