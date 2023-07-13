import agents.Scenarios.proposal_review_scenario as prs

def test_scenario_integration(proposal_id):
    scenario = prs.ProposalReviewScenario(prs.memory_stream)

    print(f'\n*** Running scenario for proposal {proposal_id} ***')

    print('\nStep 1: Reviewing the initial proposal...')
    initial_review = scenario.review_initial_proposal(proposal_id)
    print(f'The initial review is: {initial_review}')

    print('\nStep 2: Requesting updates...')
    update_request = scenario.request_updates(proposal_id)
    print(f'The update request is: {update_request}')

    print('\nStep 3: Reviewing the updated proposal...')
    updated_review = scenario.review_updated_proposal(proposal_id)
    print(f'The updated review is: {updated_review}')

    print('\nStep 4: Voting on the proposal...')
    vote = scenario.vote_on_proposal(proposal_id)
    print(f'The vote is: {vote}')

test_scenario_integration('proposal_1')
