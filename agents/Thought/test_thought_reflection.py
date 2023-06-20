from thought import Thought, Reflection

def test_thought():
    thought_type = "example"
    content = "This is an example thought"
    timestamp = "2023-07-05T14:30:10Z" # an example timestamp

    thought = Thought(thought_type, content, timestamp)
    assert thought.type == thought_type
    assert thought.content == content
    assert thought.timestamp == timestamp

def test_reflection():
    thought_type = "reflection"
    content = "This is an example reflection"
    timestamp = "2023-07-05T14:30:10Z" # an example timestamp
    memories_used = []
    reflections_used = []

    reflection = Reflection(content, timestamp, memories_used, reflections_used)
    assert reflection.type == thought_type
    assert reflection.content == content
    assert reflection.timestamp == timestamp
    assert reflection.memories_used == memories_used
    assert reflection.reflections_used == reflections_used
