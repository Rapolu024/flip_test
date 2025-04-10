from .base_task import BaseTask

class SearchTask(BaseTask):
    def run(self, product_name):
        return self.agent.act(product_name)
