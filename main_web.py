# main_web.py

from fastapi import FastAPI, Form, Request
from pydantic import BaseModel
from agents.search_agent import SearchAgent
from agents.evaluator_agent import EvaluatorAgent
from agents.notifier_agent import NotifierAgent
from tasks.search_task import SearchTask
from tasks.evaluate_task import EvaluateTask
from tasks.notify_task import NotifyTask
from fastapi.responses import HTMLResponse

app = FastAPI()

# Create model for product request
class ProductRequest(BaseModel):
    name: str

# Instantiate agents and tasks
search_task = SearchTask(SearchAgent())
evaluate_task = EvaluateTask(EvaluatorAgent())
notify_task = NotifyTask(NotifierAgent())

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>Price Negotiator</title>
        </head>
        <body>
            <h1>Price Negotiator</h1>
            <form action="/negotiate" method="post">
                <label for="product_name">Product Name:</label><br>
                <input type="text" id="product_name" name="product_name"><br><br>
                <input type="submit" value="Negotiate">
            </form>
        </body>
    </html>
    """

@app.post("/negotiate")
async def negotiate_price(product_name: str):
    # Run tasks
    result = search_task.run(product_name)  # Scrape the product data
    suggestion = evaluate_task.run(result)  # Evaluate the counter-offer
    notify_task.run(f"Negotiation for {product_name}:\n{suggestion}")  # Send a notification

    return {
        "product": product_name,
        "suggested_offer": suggestion
    }
