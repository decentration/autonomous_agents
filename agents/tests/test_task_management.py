from autonomous_agents.agents.memory_stream import MemoryStream
from autonomous_agents.agents.memory import Memory, Observation, Plan, Ideal, Reflection
from datetime import datetime, timezone, timedelta
from autonomous_agents.agents.utils import print_memory_item, ConsoleColor

def test_task_management():
    memory_stream = MemoryStream()

    current_time = datetime.now(timezone.utc)

    # Create plan memories
    plan_memory_individual = Plan(content="Write a blog post about AI", timestamp=current_time, importance=5)
    plan_memory_team = Plan(content="Develop a new AI-based feature", timestamp=current_time, importance=7)
    plan_memory_organizational = Plan(content="Expand AI research department", timestamp=current_time, importance=8)

    # Add plan memories to memory stream
    memory_stream.add_memory(plan_memory_individual, plan_level='individual')
    memory_stream.add_memory(plan_memory_team, plan_level='team')
    memory_stream.add_memory(plan_memory_organizational, plan_level='organizational')

    # Check if the tasks were added to the correct task managers
    assert len(memory_stream.individual_task_manager.tasks) == 1, "Individual task not added"
    assert len(memory_stream.team_task_manager.tasks) == 1, "Team task not added"
    assert len(memory_stream.organization_task_manager.tasks) == 1, "Organizational task not added"

    # Check if the tasks are the correct ones
    assert memory_stream.individual_task_manager.tasks[0].content == plan_memory_individual.content, "Incorrect individual task added"
    assert memory_stream.team_task_manager.tasks[0].content == plan_memory_team.content, "Incorrect team task added"
    assert memory_stream.organization_task_manager.tasks[0].content == plan_memory_organizational.content, "Incorrect organizational task added"

    print("All tests passed!")

test_task_management()
