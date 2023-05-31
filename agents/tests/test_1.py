from memory_stream import MemoryStream
from memory import Memory, Observation, Plan, Ideal, Reflection
from datetime import datetime, timezone, timedelta
from utils import print_memory_item, ConsoleColor


# 1. Create a memory stream and populate it with some initial memory items
memory_stream = MemoryStream()

current_time = datetime.now(timezone.utc)


memory_stream.add_memory(Observation(content='Klaus Mueller is discussing his research with a colleague', timestamp=current_time - timedelta(minutes=60), importance=6))
memory_stream.add_memory(Plan(content='Klaus plans to meet with his research team later today', timestamp=current_time - timedelta(minutes=30), importance=5))
memory_stream.add_memory(Ideal(content='Klaus believes in the power of collaboration to advance scientific discovery', timestamp=current_time - timedelta(minutes=15), importance=9))

memory_stream.ann_index.build(10)

# Reflection 🪞
# 2. Add new memory items and check if the reflection generation process works correctly
new_memory_item = Observation(content='Klaus has just finished a successful research presentation', timestamp='2023-04-10 14:00:00', importance=7)
memory_stream.add_memory(new_memory_item)

# The reflection generation process should be executed automatically when adding a new memory item
# You can verify the reflections by checking the content of the memory_stream.memories and memory_tree.nodes

# 3. Test the `retrieve_memory` function by providing different query inputs
query = 'What was Klaus doing earlier today?'
print("\nRetrieving memories for query 1")
retrieved_memories = memory_stream.retrieve_memory(query, datetime.now(timezone.utc))


# Check if the retrieved memories match the expected results (e.g., the memory about Klaus discussing his research)
for memory in retrieved_memories:
    print("Query 1:", end=" ")
    print_memory_item(memory)


# 4. Test the collaboration between agents by simulating a conversation between them and checking if they can share and access the memory stream
# You can use the chat API to simulate a conversation and have the agents share information stored in the memory stream

# Depending on the agent's behavior, you can simulate different scenarios where agents access and modify the memory stream
# Test with a query about Klaus's plans
query2 = "What are Klaus's plans for the conference?"
retrieved_memories2 = memory_stream.retrieve_memory(query2, datetime.now(timezone.utc))

for memory in retrieved_memories2:
    print(f"Query 2:", memory.symbol, memory.timestamp, memory.type, ConsoleColor.GREEN, "importance:",  memory.importance, ConsoleColor.RESET, memory.content)

# Test with a query about Klaus's research and a specific timeframe (e.g., the last hour)
query3 = "What happened in Klaus's research in the last hour?"
retrieved_memories3 = memory_stream.retrieve_memory(query3, datetime.now(timezone.utc))

for memory in retrieved_memories3:
    print("Query 3:", memory.symbol, memory.content)


# Step 2: Implement a function that generates a new reflection based on the evidence provided
def generate_reflection(memory_stream, content, timestamp, importance, evidence_ids):
    evidence = []
    for memory_id in evidence_ids:
        memory = memory_stream.get_memory_by_id(memory_id)
        if memory is not None:
            evidence.append(memory)  # Add the memory object instead of its content
    reflection = Reflection(content=content, timestamp=timestamp, importance=importance, evidence=evidence)
    memory_stream.add_memory(reflection)
    return reflection


# Test the generate_reflection function
# new_reflection = generate_reflection(memory_stream, content='Klaus is dedicated to advancing scientific knowledge', timestamp='2023-04-10 13:30:00', importance=7, evidence_ids=[1, 2])

memory_object = memory_stream.get_memory_by_id("df700b1c-dcf3-4bcd-bce1-d1db53272d7c")
if memory_object is not None:
    new_reflection = Reflection(content="Klaus is good at presentations", timestamp="2023-04-10 15:00:00", importance=8, evidence=[memory_object])


# Step 3: Test the retrieval function with different queries
query1 = 'What was Klaus doing earlier today?'
print("\nRetrieving memories for query 1")
retrieved_memories1 = memory_stream.retrieve_memory(query1, datetime.now(timezone.utc))
print("\nQuery 1 results:")
for memory in retrieved_memories1:
    print(f"Query 1:", memory.symbol, memory.timestamp, memory.type, ConsoleColor.GREEN, "importance:",  memory.importance, ConsoleColor.RESET, memory.content)

query2 = 'What are Klaus\'s beliefs?'
retrieved_memories2 = memory_stream.retrieve_memory(query2, datetime.now(timezone.utc))
print("\nQuery 2 results:")
for memory in retrieved_memories2:
    print(f"Query 2:", memory.symbol, memory.timestamp, memory.type, ConsoleColor.GREEN, "importance:",  memory.importance, ConsoleColor.RESET, memory.content)

query3 = 'What are the reflections about Klaus?'
retrieved_memories3 = memory_stream.retrieve_memory(query3, datetime.now(timezone.utc))
print("\nQuery 3 results:")
for memory in retrieved_memories3:
    print(f"Query 3:", memory.symbol, memory.timestamp, memory.type, ConsoleColor.GREEN, "importance:",  memory.importance, ConsoleColor.RESET, memory.content)
