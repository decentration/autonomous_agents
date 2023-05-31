from agents.autonomous_agent import AutonomousAgent
from agents.memory import Observation, Plan, Reflection
from autonomous_agents.agents.utils import save_agent_instance

# Create an agent instance
agent = AutonomousAgent("instance_id_1", agent_roles={"role": "manager"}, agent_mission="Increase sales by 10%")

# Add memory objects
agent.create_observation("Observed a decline in sales", 0.5, "2023-04-01")
agent.create_plan("Plan to improve marketing", 0.7, "2023-04-02")
agent.create_reflection("Reflecting on the recent sales strategy", 0.8, "2023-04-03")

# Save agent instance
agent_instance_data = {
    "instance_id": agent.instance_id,
    "agent_roles": agent.agent_roles,
    "agent_mission": agent.agent_mission,
    "memory_stream": [memory.__dict__ for memory in agent.memory_stream.nodes]
}

save_agent_instance(agent_instance_data)
