from utils.notifier import send_notification
from .base_agent import BaseAgent

class NotifierAgent(BaseAgent):
    def act(self, message):
        # This will send the notification to the user.
        return send_notification(message)
