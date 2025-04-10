class BaseAgent:
    def __init__(self):
        pass

    def act(self, data):
        raise NotImplementedError("Subclasses must implement act method")
