from .base_task import BaseTask

class NotifyTask(BaseTask):
    def run(self, message):
        return self.agent.act(message)
