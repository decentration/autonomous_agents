import proposal_review_scenario_dummy as prs
from agents.Memory.memory_stream import MemoryStream  # Import MemoryStream


def test_scenario(proposal_id):

     # Creating an instance of the MemoryStream class
    memory_stream = MemoryStream()

    # Creating an instance of the ProposalReviewScenario class
    scenario = prs.ProposalReviewScenario(memory_stream)  # Pass the MemoryStream instance

    print(f'\n*** Running scenario for proposal {proposal_id} ***')

    # 1. Review the initial proposal
    print('\nStep 1: Reviewing the initial proposal...')
    initial_review = scenario.review_initial_proposal(proposal_id)
    print(f'The initial review is: {initial_review}')

    # 2. Request for updates
    print('\nStep 2: Requesting updates...')
    update_request = scenario.request_updates(proposal_id)
    print(f'The update request is: {update_request}')

    # 3. Review updated proposal
    print('\nStep 3: Reviewing the updated proposal...')
    updated_review = scenario.review_updated_proposal(proposal_id)
    print(f'The updated review is: {updated_review}')

    # 4. Voting on the proposal
    print('\nStep 4: Voting on the proposal...')
    vote = scenario.vote_on_proposal(proposal_id)
    print(f'The vote is: {vote}')



# Run the test scenario for a given proposal
test_scenario('proposal_1')
