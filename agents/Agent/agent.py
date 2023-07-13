class Agent:
    def __init__(self, memory_stream, thought_stream, action_stream, system_message):
        self.memory_stream = memory_stream
        self.thought_stream = thought_stream
        self.action_stream = action_stream
        self.system_message = system_message
        self.active_scenarios = {}

    def join_scenario(self, scenario):
        self.active_scenarios[scenario.id] = scenario

    def leave_scenario(self, scenario_id):
        del self.active_scenarios[scenario_id]

    # ... add additional methods to manage memory, thoughts, and actions
