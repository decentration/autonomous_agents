from memory_stream import MemoryStream
from memory import Memory, Observation, Plan, Ideal, Reflection
from datetime import datetime, timezone, timedelta
from utils import print_memory_item, ConsoleColor
from reflection_tree import ReflectionTree

class SimpleGPTAgent:
    def generate_reflection(self, evidence_memories):
        reflection_content = "Generated reflection based on provided evidence."
        return reflection_content
    def generate_importance(self):
        # Implement the logic to generate an importance value
        importance = 8  # Placeholder
        return importance

memory_stream = MemoryStream()

# Instantiate the SimpleGPTAgent
gpt_agent = SimpleGPTAgent()

current_time = datetime.now(timezone.utc)

memory_stream.add_memory(Observation(content='Klaus Mueller is discussing his research with a colleague', timestamp=current_time - timedelta(minutes=60), importance=6))
memory_stream.add_memory(Plan(content='Klaus plans to meet with his research team later today', timestamp=current_time - timedelta(minutes=30), importance=5))
memory_stream.add_memory(Ideal(content='Klaus believes in the power of collaboration to advance scientific discovery', timestamp=current_time - timedelta(minutes=15), importance=9))

memory_stream.ann_index.build(10)

query = 'What was Klaus doing earlier today?'
retrieved_memories = memory_stream.retrieve_memory(query, datetime.now(timezone.utc))

for memory in retrieved_memories:
    memory.update_last_viewed(datetime.now(timezone.utc))  # Update the last_viewed attribute
    print_memory_item(memory)


# Test the generate_reflection_from_evidence function
reflection_tree = ReflectionTree()
reflection_importance = gpt_agent.generate_importance()
reflection_timestamp = datetime.now(timezone.utc)
generated_reflection = reflection_tree.generate_reflection_from_evidence(retrieved_memories, gpt_agent, reflection_importance, reflection_timestamp)

query4 = 'What are the reflections about Klaus?'
retrieved_memories4 = memory_stream.retrieve_memory(query4, datetime.now(timezone.utc))
print("\nQuery 4 results:")
for memory in retrieved_memories4:
    print_memory_item(memory)

# Test if the reflection is properly stored in the ReflectionTree and if the evidence is correctly linked to the reflection
query2 = 'What are the reflections about Klaus?'
retrieved_reflections = reflection_tree.retrieve_memory(query2, datetime.now(timezone.utc))

print("\nRetrieving reflections")
for memory in retrieved_reflections:
    print_memory_item(memory)
    if isinstance(memory, Reflection) and memory.evidence:
        print("  Evidence:")
        for evidence_memory in memory.evidence:
            print("   >", end=" ")
            print_memory_item(evidence_memory)
