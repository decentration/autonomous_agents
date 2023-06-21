# Define the dummy data
proposals = {
    '123': {
        'initial': 'This is the initial proposal text.',
        'updated': 'This is the updated proposal text with more budget details.',
    },
    '124': {
        'initial': 'This is another initial proposal text.',
        'updated': 'This is the updated proposal text with new strategy details.',
    }
}

# Simulate the steps
def simulate_scenario(proposal_id):
    print(f'\n*** Reviewing proposal {proposal_id} ***')
    # 1. Review the initial proposal
    print('Reviewing the initial proposal...')
    initial_proposal = proposals[proposal_id]['initial']
    initial_feedback = f'The initial proposal is: {initial_proposal}'
    print(initial_feedback)

    # 2. Request an update
    print('Requesting an update...')
    update_request = 'Could you please provide more details?'
    print(update_request)

    # 3. Review the updated proposal
    print('Reviewing the updated proposal...')
    updated_proposal = proposals[proposal_id]['updated']
    updated_feedback = f'The updated proposal is: {updated_proposal}'
    print(updated_feedback)

    # 4. Vote on the proposal
    print('Voting on the proposal...')
    vote = 'Yes'
    print(f'I vote {vote} on the proposal.')

# Run the simulation
simulate_scenario('123')
simulate_scenario('124')
