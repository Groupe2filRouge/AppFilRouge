import requests
import json

# The service for messaging operations
class MessagingService():

    # Constructor
    def __init__(self):
        print("init MessagingService")

    # Test method for slack messages
    def testSlack(self):
        blocks = [
            {  
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Hello, Assistant to the Regional Manager Dwight! *Michael Scott* wants to know where you'd like to take the Paper Company investors to dinner tonight.\n\n *Please select a restaurant:*"
            }
            }
        ]

        return self.post_message_to_slack("Text shown in popup.", blocks)

    # Post a given block message
    def post_message_to_slack(self, text, blocks = None):
        return requests.post('https://slack.com/api/chat.postMessage', {
            'text': text,
            'icon_emoji': ':see_no_evil:',
            'username': "botfilrouge",
            'blocks': json.dumps(blocks) if blocks else None
        }).json()	
