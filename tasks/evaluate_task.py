from .base_task import BaseTask

class EvaluateTask(BaseTask):
    def run(self, product_data):
        return self.agent.act(product_data)
