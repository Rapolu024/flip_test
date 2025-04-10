class BaseTask:
    def __init__(self, agent):
        self.agent = agent

    def run(self, input_data):
        raise NotImplementedError("Subclasses must implement run method")
