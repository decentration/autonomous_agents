from agents.Memory.memory_stream import MemoryStream
from agents.Memory.memory import Memory, Observation, Plan, Ideal
from agents.Thought.thought import Reflection
from agents.Action.action import Action, Operational
from datetime import datetime, timezone, timedelta
from agents.utils import print_memory_item, ConsoleColor

memory_stream = MemoryStream()
current_time = datetime.now(timezone.utc)

class ProposalReviewScenario:
    def __init__(self, memory_stream):
        self.memory_stream = memory_stream
        self.scenario_status = 0  # 0: Initial Review, 1: Update Request, 2: Review Updated Proposal, 3: Vote
        self.proposal = {
            'id': None,
            'feedback': []
        }

    def generate_response(self, prompt):
        # For now, this function just returns the prompt.
        # In the next stage, replace this with an actual call to the GPT-4 model
        return f"Response to: {prompt}"

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
        feedback = self.generate_response("Provide feedback on 'Proposal X'...")

         # Add feedback to the memory stream
        feedback_observation = Observation(content=feedback, timestamp=datetime.now(timezone.utc), importance=8)
        self.memory_stream.add_memory(feedback_observation)

        # Add feedback to the proposal
        self.proposal['id'] = proposal_id
        self.proposal['feedback'].append(feedback)

        self.update_scenario_status()
        return feedback

    def request_updates(self, proposal_id):
        if self.scenario_status != 1:
            raise Exception("This is not the correct step in the scenario")

        # Retrieve the feedback from the proposal
        feedback = self.proposal['feedback'][-1]  

        # Generate a request for an update based on the proposal and feedback
        update_request = self.generate_response(f"Based on the feedback ('{feedback}'), what updates are needed for 'Proposal X'?")

        # Add request to the memory stream
        update_request_plan = Plan(content=update_request, timestamp=datetime.now(timezone.utc), importance=8, level='team')
        self.memory_stream.add_memory(update_request_plan)

        self.update_scenario_status()
        return update_request

    def review_updated_proposal(self, proposal_id):
        if self.scenario_status != 2:
            raise Exception("This is not the correct step in the scenario")

        # Generate a review based on the updated proposal
        updated_review = self.generate_response("Review the updated 'Proposal X'...")

        # Add review to the memory stream
        updated_review_observation = Observation(content=updated_review, timestamp=datetime.now(timezone.utc), importance=8)
        self.memory_stream.add_memory(updated_review_observation)

        # Add feedback to the proposal
        self.proposal['feedback'].append(updated_review)

        self.update_scenario_status()
        return updated_review

    def vote_on_proposal(self, proposal_id):
        if self.scenario_status != 3:
            raise Exception("This is not the correct step in the scenario")

        # Generate a vote based on the final review
        vote = self.generate_response("Based on the final review, vote 'yes' or 'no' for 'Proposal X'...")

        # Add vote to the memory stream as an action
        vote_action = Operational(content=vote, timestamp=datetime.now(timezone.utc), associated_task=None, operations="Reviewing and voting on proposals")
        self.memory_stream.add_memory(vote_action)

        self.update_scenario_status()
        return vote


# Initialize scenario
scenario = ProposalReviewScenario(memory_stream)

# Simulate endpoint calls
scenario.review_initial_proposal(proposal_id="dummy_id")
scenario.request_updates(proposal_id="dummy_id")
scenario.review_updated_proposal(proposal_id="dummy_id")
scenario.vote_on_proposal(proposal_id="dummy_id")
