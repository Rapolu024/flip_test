import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = "your_openai_api_key_here"

def generate_counter_offer(product_name, current_price, seller_note):
    prompt = f"""
    You are an expert e-commerce price negotiator. The following product has been found:

    Product: {product_name}
    Price: {current_price}
    Seller Note: {seller_note}

    Suggest a reasonable counter-offer price and reasoning.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7
    )
    return response.choices[0].text.strip()
