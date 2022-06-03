import requests
from devops_utils.logging import *
import json

class Slack():

    def __init__(self):
        self.webhook_base = "https://hooks.slack.com/services"
        self.test_message = {'blocks': [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Test Message"
                    }
                }
            ]}

    def notify_webhook(self,slack_channel, slack_hook,message=None):
        if not message:
            message = self.test_message
            
        webhook_url = f"{self.webhook_base}/{slack_hook.strip()}"
        slack_data = json.dumps({**message , **{"channel": slack_channel, "as_user": True}})
        response = requests.post(webhook_url,
                                data=slack_data,
                                headers={'Content-Type': 'application/json'})
        
        if response.status_code != 200:
            logger.error("Failed to post slack message to {} - {}".format(slack_channel,json.dumps(response.text)))
            return False
        
        return True