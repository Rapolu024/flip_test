from utils.scraper import scrape_amazon, scrape_flipkart
from .base_agent import BaseAgent

class SearchAgent(BaseAgent):
    def act(self, product_name):
        # Search for the product in Amazon and Flipkart
        amazon_data = scrape_amazon(product_name)
        flipkart_data = scrape_flipkart(product_name)
        
        return {
            "amazon": amazon_data,
            "flipkart": flipkart_data
        }
