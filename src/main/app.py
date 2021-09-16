from flask import Flask, render_template, request
import json

# Import services
from services.cloudService import CloudService
from services.converterService import ConverterService
from services.databaseService import DatabaseService
from services.messagingService import MessagingService
from services.gitService import GitService

# Instanciate services
cloudSrv = CloudService()
converterSrv = ConverterService()
databaseSrv = DatabaseService()
messagingSrv = MessagingService()
gitSrv = GitService()

# Create app Flask
app = Flask(__name__)

# The webhook adress for a git account
@app.route("/github-webhook/", methods=["POST"])
def webhook():
    popup_text = "Un rédacteur vient de pousser du contenu sur GitHub"    
    data = json.loads(request.data)   
    redacteur = databaseSrv.get_redacteur_data(data['repository']['clone_url'], data['ref'])[0]
    # TODO - cas non trouve
    author = data['commits'][0]['author']['name']
    # blocks = messagingSrv.format_git_slack_message(data['commits'][0]['author']['name'], redacteur)        
    # messagingSrv.post_message_to_slack(redacteur['slackToken'].strip('"'), redacteur['slackChannel'].strip('"'), popup_text, blocks)
    text_block = "{} vient de mettre à disposition son travail.".format(author)
    messagingSrv.post_message(redacteur['slackToken'].strip('"'), redacteur['slackChannel'].strip('"'), popup_text, text_block, redacteur['gitProjectName'], redacteur['gitAdress'])
    gitSrv.clone(redacteur['gitAdress'], redacteur['gitBranchName'], redacteur['gitBranch'], redacteur['gitProjectName'])
    converterSrv.convert(redacteur['gitProjectName'])  
    cloudSrv.push(redacteur['s3Name'], redacteur['gitProjectName']) 
    # blocks = messagingSrv.format_s3_slack_message(data['commits'][0]['author']['name'], redacteur)        
    # messagingSrv.post_message_to_slack(redacteur['slackToken'].strip('"'), redacteur['slackChannel'].strip('"'), popup_text, blocks)
    text_block = "Les fichiers convertis sont disponibles sur l'espace de stockage."
    text_attachement = "{}/{}".format(redacteur['s3Adress'], redacteur['s3Name'])
    messagingSrv.post_message(redacteur['slackToken'].strip('"'), redacteur['slackChannel'].strip('"'), popup_text, text_block, redacteur['s3Name'], text_attachement)
    return "Done"

@app.route("/", methods=["GET"])
def home():
    return "AppFilRouge " + databaseSrv.get_nb_redacteur_data()

# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run(host= '0.0.0.0')
