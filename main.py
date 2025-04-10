import json
from agents.search_agent import SearchAgent
from agents.evaluator_agent import EvaluatorAgent
from agents.notifier_agent import NotifierAgent
from tasks.search_task import SearchTask
from tasks.evaluate_task import EvaluateTask
from tasks.notify_task import NotifyTask

with open("data/products.json") as f:
    products = json.load(f)

# Instantiate agents and tasks
search_task = SearchTask(SearchAgent())
evaluate_task = EvaluateTask(EvaluatorAgent())
notify_task = NotifyTask(NotifierAgent())

# Loop over the products, scrape, evaluate, and notify
for product in products:
    result = search_task.run(product["name"])  # Scrape the product data
    suggestion = evaluate_task.run(result)     # Get the negotiation suggestion
    notify_task.run(f"{product['name']} Suggestion:\n{suggestion}")  # Send the notification
