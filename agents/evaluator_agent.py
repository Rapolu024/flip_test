from utils.nlp_engine import generate_counter_offer
from .base_agent import BaseAgent

class EvaluatorAgent(BaseAgent):
    def act(self, product_data):
        # Extract data for negotiation from both Amazon and Flipkart
        amazon_data = product_data['amazon']
        flipkart_data = product_data['flipkart']

        # Evaluate counter-offer for Amazon and Flipkart prices
        amazon_offer = generate_counter_offer(amazon_data['name'], amazon_data['price'], amazon_data['note'])
        flipkart_offer = generate_counter_offer(flipkart_data['name'], flipkart_data['price'], flipkart_data['note'])

        return {
            "amazon_offer": amazon_offer,
            "flipkart_offer": flipkart_offer
        }
