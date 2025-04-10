from telegram.ext import Updater, CommandHandler
from agents.search_agent import SearchAgent
from agents.evaluator_agent import EvaluatorAgent
from agents.notifier_agent import NotifierAgent
from tasks.search_task import SearchTask
from tasks.evaluate_task import EvaluateTask
from tasks.notify_task import NotifyTask

# telegram_bot.py

import os
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Telegram bot setup continues...


# Instantiate agents and tasks
search_task = SearchTask(SearchAgent())
evaluate_task = EvaluateTask(EvaluatorAgent())
notify_task = NotifyTask(NotifierAgent())

def start(update, context):
    update.message.reply_text("Welcome to the Price Negotiator Bot! Use /check <product_name>")

def check(update, context):
    product_name = " ".join(context.args)
    result = search_task.run(product_name)  # Scrape product data
    suggestion = evaluate_task.run(result)  # Evaluate the counter-offer
    notify_task.run(f"Negotiation for {product_name}:\n{suggestion}")  # Send a notification
    update.message.reply_text(f"Negotiation for {product_name}:\n{suggestion}")

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("check", check))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()