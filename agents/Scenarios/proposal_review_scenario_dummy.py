from agents.Memory.memory_stream import MemoryStream
from agents.Memory.memory import Memory, Observation, Plan, Ideal
from agents.Thought.thought import Reflection
from datetime import datetime, timezone, timedelta
from agents.utils import print_memory_item, ConsoleColor

memory_stream = MemoryStream()
current_time = datetime.now(timezone.utc)

class ProposalReviewScenario:
    def __init__(self, memory_stream):
        self.memory_stream = memory_stream
        self.scenario_status = 0  # 0: Initial Review, 1: Update Request, 2: Review Updated Proposal, 3: Vote

    def update_scenario_status(self):
        self.scenario_status += 1

    def review_initial_proposal(self, proposal_id):
        if self.scenario_status != 0:
            raise Exception("This is not the correct step in the scenario")
        # Add context and instructions to memory_stream
        context = Observation(content="You are about to review a proposal titled 'Proposal X'. Consider the following points while giving your feedback...", timestamp=datetime.now(timezone.utc), importance=10)
        self.memory_stream.add_memory(context)
        instructions = Plan(content="Your task is to provide constructive feedback on 'Proposal X'. Remember to consider its relevance, feasibility, and potential impact.", timestamp=datetime.now(timezone.utc), importance=10, level='team')
        self.memory_stream.add_memory(instructions)
        # Now the agent can execute the task based on the new context and instructions
        # Generate feedback based on the proposal
        # Add feedback to the memory stream
        self.update_scenario_status()
        return "Initial review completed"  # Replace with actual feedback

    def request_updates(self, proposal_id):
        if self.scenario_status != 1:
            raise Exception("This is not the correct step in the scenario")
        # Retrieve the proposal and feedback from memory
        # Generate a request for an update based on the proposal and feedback
        # Add request to the memory stream
        self.update_scenario_status()
        return "Update request sent"  # Replace with actual request

    def review_updated_proposal(self, proposal_id):
        if self.scenario_status != 2:
            raise Exception("This is not the correct step in the scenario")
        
        # Now the agent can execute the tasks based on the new context and hardcoded instructions
        instruction1 = "Review the updated proposal and make a judgment."
        response1 = "Generated response to instruction1"  # Placeholder response
        
        context = Observation(content='The agent provided feedback on the proposal.', timestamp=datetime.now(timezone.utc), importance=7)
        self.memory_stream.add_memory(context)

        instruction2 = "Provide your final review of the proposal in text."
        response2 = "Generated response to instruction2"  # Placeholder response

        context = Observation(content='The agent requested an update on the proposal.', timestamp=datetime.now(timezone.utc), importance=7)
        self.memory_stream.add_memory(context)

        self.update_scenario_status()

        return "Updated review completed"

    def vote_on_proposal(self, proposal_id):
        if self.scenario_status != 3:
            raise Exception("This is not the correct step in the scenario")

        instruction = "Make a concrete vote of 'yes' or 'no' on the proposal."
        response = "Generated response to instruction"  # Placeholder response

        context = Observation(content='The agent reviewed the proposal and voted.', timestamp=datetime.now(timezone.utc), importance=7)
        self.memory_stream.add_memory(context)

        self.update_scenario_status()

        return "Vote completed"



# Initialize scenario
scenario = ProposalReviewScenario(memory_stream)

# Simulate endpoint calls
scenario.review_initial_proposal(proposal_id="dummy_id")
scenario.request_updates(proposal_id="dummy_id")
# scenario.review_updated_proposal(proposal_id="dummy_id")
# scenario.vote_on_proposal(proposal_id="dummy_id")