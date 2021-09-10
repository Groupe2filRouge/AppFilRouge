import requests
import json

#For credentials
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv('../.env')

# The service for messaging operations
class MessagingService():

    # Constructor
    def __init__(self):
        print("init MessagingService")

    # Format slack message
    def format_slack_message(self, git_data, redacteur_data):
        blocks = [
            {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Le rédacteur {} vient de pousser un fichier Markdown\
                 sur le repository Git suivant.".format(git_data['commits'][0]['author']['name'])
            }
            },             
            {  
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "{}".format(redacteur_data['gitAdress'])
            }
            },
            {  
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Le(s) fichiers converti(s) en HTML sont disponible(s)\
                 sur Amazon cloud sur l'espace de stockage {}".format(redacteur_data['s3Name'])
            }
            }
        ]
        return blocks
        

    # Post a given block message
    def post_message_to_slack(self, token, canal, text, blocks):
        return requests.post('https://slack.com/api/chat.postMessage', {
            'token': token,
            'channel': canal,
            'text': text,
            'icon_emoji': ':see_no_evil:',
            'username': "botfilrouge",
            'blocks': json.dumps(blocks) if blocks else None
        }).json()	
