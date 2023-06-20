from action import Action, Strategic, Operational, Management, Communication, Development

def test_action():
    action_type = "example"
    content = "This is an example action"
    timestamp = "2023-07-05T14:30:10Z" # an example timestamp
    associated_task = "example_task"

    action = Action(action_type, content, timestamp, associated_task)
    assert action.type == action_type
    assert action.content == content
    assert action.timestamp == timestamp
    assert action.associated_task == associated_task

# Similarly, you can create tests for the subclasses of Action like Strategic, Operational, etc.
