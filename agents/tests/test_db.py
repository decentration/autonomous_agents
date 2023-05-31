from memory_stream import MemoryStream
from memory import Memory, Reflection, Observation, Plan, Ideal
from memory_database import MemoryDatabase
from datetime import datetime, timezone, timedelta


# Initialize the MemoryStream and MemoryDatabase instances
memory_stream = MemoryStream()
memory_db = MemoryDatabase()

# Add memories to the memory_stream
current_time = datetime.now(timezone.utc)

memory1 = Observation(content='Alice just proposed a referendum #35 🗳️', timestamp=current_time - timedelta(minutes=60), importance=7)
memory2 = Plan(content='Bob is planning a new project', timestamp=current_time - timedelta(minutes=30), importance=4)
memory3 = Ideal(content='Charlie thinks that teamwork is essential', timestamp=current_time - timedelta(hours=2), importance=8)
memory4 = Reflection(content='Though Alice values collaboration, in her values tree she allows for discretion on urgent matters.', timestamp=current_time - timedelta(days=1), importance=6, evidence=['memory1_id', 'memory3_id'])

memories = [memory1, memory2, memory3, memory4]

for memory in memories:
    memory_stream.add_memory(memory)
    memory_db.insert_memory(memory)

# Retrieve all memories from the MemoryDatabase
all_memories = memory_db.get_memories()

print("All memories retrieved from the database:")
for memory in all_memories:
    print(f"{memory.symbol}{memory.id}: {memory.content}")

# Test the retrieve_memory function with a query
query = 'What was Alice working on today?'
print(f"\nRetrieving memories for query: {query}")

retrieved_memories = memory_stream.retrieve_memory(query, datetime.now(timezone.utc))

for memory in retrieved_memories:
    print(f"{memory.symbol} Memory ID: {memory.id}, Content: {memory.content}")

# Close the connection to the database
memory_db.close()