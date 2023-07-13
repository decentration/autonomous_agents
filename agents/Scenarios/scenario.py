from memory_stream import MemoryStream


class Scenario:
    def __init__(self):
        self.memory_stream = MemoryStream()
        self.actions = []
        self.feedback = {}
        self.proposal_id = None
        # and any other data that is necessary for the scenario

    # then all your scenario methods go here, 
    # operating on the data contained within the instance
