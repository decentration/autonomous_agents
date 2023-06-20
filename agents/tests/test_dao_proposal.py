from agents.Memory.memory_stream import MemoryStream
from agents.Memory.memory import Memory, Observation, Plan, Ideal
from agents.Thought.thought import Reflection
from datetime import datetime, timezone, timedelta
from agents.utils import print_memory_item, ConsoleColor



def generate_reflection(memory_stream, content, timestamp, importance, evidence_ids):
    evidence = []
    for memory_id in evidence_ids:
        memory = memory_stream.get_memory_by_id(memory_id)
        if memory is not None:
            evidence.append(memory)  # Add the memory object instead of its content
    reflection = Reflection(content=content, timestamp=timestamp, importance=importance, evidence=evidence)
    memory_stream.add_memory(reflection)
    return reflection

# 1. Create a memory stream and populate it with some initial memory items
memory_stream = MemoryStream()

current_time = datetime.now(timezone.utc)


memory_stream.add_memory(Observation(content='Dave made a funding proposal #39 💰🗳️', timestamp=current_time - timedelta(minutes=60), importance=9))
memory_stream.add_memory(Observation(content='Eve made a funding proposal #40 💰🗳️', timestamp=current_time - timedelta(minutes=58), importance=5, ))
memory_stream.add_memory(Plan(content='A calendar invite was requested 4th June 3:00 for Alice to review funding proposal #39 💰🗳️ ', timestamp=current_time - timedelta(minutes=30), importance=7, level='organization'))
memory_stream.add_memory(Observation(content='The funding proposal review for #39 has no collisions, and was auto accepted', timestamp=current_time - timedelta(minutes=28), importance=7))

memory_stream.add_memory(Observation(content='The funding proposal review for #39 has no collisions, and was auto accepted', timestamp=current_time - timedelta(minutes=28), importance=7))
memory_stream.add_memory(Plan(content='A calendar invite was requested 4th June 3:20 for Alice to review funding proposal #40 💰🗳️ ', timestamp=current_time - timedelta(minutes=27), importance=7, level='organization'))
memory_stream.add_memory(Observation(content='The funding proposal review for #40 has no collisions, and was auto accepted', timestamp=current_time - timedelta(minutes=26), importance=7))
memory_stream.add_memory(Plan(content='Alice set up a meeting (#112) on 1st June 2023 in the Group Calendar, at 3pm UTC, to explore the proposed referendum #35.', timestamp=current_time - timedelta(minutes=30), importance=7, level='organization'))
memory_stream.add_memory(Observation(content='The meeting (#112) has no collisions, and was auto accepted', timestamp=current_time - timedelta(minutes=25), importance=7))
memory_stream.add_memory(Ideal(content='Alice values collaboration, grassroots development and debating ideas as part of her approach to self-organisation.', timestamp=current_time - timedelta(minutes=15), importance=8))
memory_stream.add_memory(Observation(content='Alice noticed an issue (#101) in relation to GRANDPA finalization selection.', timestamp=current_time - timedelta(minutes=5), importance=9))
memory_stream.add_memory(Plan(content='Alice requests Charlie make further investigation 1st June 2023, at 3pm UTC and report back a solution and action steps.', timestamp=current_time - timedelta(minutes=3), importance=9, level='team'))
memory_stream.add_memory(Observation(content='Alice noticed a collision in Charlies timetable.', timestamp=current_time - timedelta(minutes=5), importance=6))
memory_stream.add_memory(Observation(content='Alice removed Charlie from group meeting. #[Reason] Charlie has an urgent priority matter to handle in relation to GRANDPA issue #101.', timestamp=current_time - timedelta(minutes=5), importance=6))
memory_stream.add_memory(Observation(content='Alice checked the Github repo for any available releases.', timestamp=current_time + timedelta(minutes=30), importance=6))
memory_stream.add_memory(Observation(content='Alice makes runtime upgrade referendum #36 🗳️', timestamp=current_time + timedelta(minutes=35), importance=6))
memory_stream.add_memory(Observation(content='Group memory stream: The referendum was downvoted by Bob, Dave and Ferdie downvoted the upgrade. #[Reason] There was a failure in the replicating the deterministic build.', timestamp=current_time + timedelta(minutes=55), importance=6))


# Use the generate_reflection function to create a new reflection based on the first memory item
new_reflection = generate_reflection(
    memory_stream,
    content="ReflectionNew: The referendum #35 is an important matter for the community.",
    timestamp=current_time - timedelta(minutes=50),
    importance=8,
    evidence_ids=["1"]
)

# Add the new reflection to the memory stream
memory_stream.add_memory(new_reflection)

# Verify that the reflection was added to the memory stream
print("New reflection:", end=" ")
print_memory_item(new_reflection)

# memory_stream.add_memory(Reflection(content='Though Alice values collaboration, in her values tree she allows for discretion on urgent matters.', timestamp=current_time - timedelta(minutes=5), importance=6, evidence=))

# Reflection 🪞
# 2. Add new memory items and check if the reflection generation process works correctly
new_memory_item = Observation(content='Alice requested all other agents read proposal and make initial suggestions.', timestamp=current_time - timedelta(minutes=90), importance=7)
memory_stream.add_memory(new_memory_item)

# The reflection generation process should be executed automatically when adding a new memory item
# You can verify the reflections by checking the content of the memory_stream.memories and memory_tree.nodes

# 3. Test the `retrieve_memory` function by providing different query inputs
query = 'What was Alice working on today?'
print(query)
print("\nRetrieving memories for query 1")
memory_stream.ann_index.build(10)
retrieved_memories = memory_stream.retrieve_memory(query, datetime.now(timezone.utc))

# Check if the retrieved memories match the expected results (e.g., the memory about Klaus discussing his research)
for memory in retrieved_memories:
    print("Query 1:", end=" ")
    print_memory_item(memory)


# 4. Test the collaboration between agents by simulating a conversation between them and checking if they can share and access the memory stream
# You can use the chat API to simulate a conversation and have the agents share information stored in the memory stream

# Depending on the agent's behavior, you can simulate different scenarios where agents access and modify the memory stream
# Test with a query about Klaus's plans
query2 = "☝️ What was the most urgent matter today?"
print(query2)
retrieved_memories2 = memory_stream.retrieve_memory(query2, datetime.now(timezone.utc))

for memory in retrieved_memories2:
    print("Query 2-new:", end=" ")
    print_memory_item(memory)
    # print(f"Query 2:", memory.symbol, memory.timestamp, memory.type, ConsoleColor.GREEN, "importance:",  memory.importance, ConsoleColor.RESET, memory.content)

# Test with a query about Klaus's research and a specific timeframe (e.g., the last hour)
query3 = " ☝️ What happened in Alice work in the last hour?"
print(query3)
retrieved_memories3 = memory_stream.retrieve_memory(query3, datetime.now(timezone.utc))

for memory in retrieved_memories3:
    print("Query 3:", end=" ")
    print_memory_item(memory)


# Step 2: Implement a function that generates a new reflection based on the evidence provided
memory_object = memory_stream.get_memory_by_id("df700b1c-dcf3-4bcd-bce1-d1db53272d7c")
if memory_object is not None:
   new_reflection = generate_reflection(memory_stream, "Alice is dedicated to further decentralisation, incentivise collaboration, and the health of the decentralised organsim.", timestamp=current_time + timedelta(minutes=120), importance=8, evidence_ids=[1, 2])
   memory_stream.add_memory(new_reflection)
   print_memory_item(new_reflection)

query4 = "What are some reflections about Alice's work?"
print(query4)
retrieved_memories4 = memory_stream.retrieve_memory(query4, datetime.now(timezone.utc))

for memory in retrieved_memories4:
    print("Query 4:", end=" ")
    print_memory_item(memory)

