import requests
import json
from datetime import datetime

#For credentials
#from dotenv import load_dotenv
import os

# Load .env file
#load_dotenv('../.env')

# The service for messaging operations
class MessagingService():

    # Constructor
    def __init__(self):
        print("init MessagingService")

    # Format slack message
    def format_slack_message(self, author, redacteur_data):
        print(redacteur_data)
        blocks = [
            {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Le rédacteur {} vient de pousser un fichier Markdown\
                 sur le repository Git suivant.".format(author)
            }
            },             
            {  
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": redacteur_data['gitAdress']
            }
            },
            {  
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Le(s) fichiers converti(s) en HTML sont disponible(s)\
                 sur Amazon cloud sur l'espace de stockage {}{}".format(redacteur_data['s3Adress'], redacteur_data['s3Name'])
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

    def post_message(self, token, canal, text, text_block, title, text_attachement):
        return requests.post('https://slack.com/api/chat.postMessage', {
            'token': token,
            'channel': canal,
            'username': "botfilrouge",
            'attachments': json.dumps( 
                [
                    {
                        "fallback": "Required plain-text summary of the attachment.",
                        "color": "#36a64f",
                        "pretext": text_block,
                        "title": title,
                        "title_link": text_attachement,
                        "image_url": "http://my-website.com/path/to/image.jpg",
                        "thumb_url": "http://example.com/path/to/thumb.png",
                        "footer": "Converter API",
                        "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
                        "ts": datetime.timestamp(datetime.now())
                    }
                ]
            )
        }).json()	
