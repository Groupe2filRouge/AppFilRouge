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

# Annotation that allows the function to be hit at the specific URL.
@app.route("/")
# Generic Python functino that returns "Hello world!"
def index():
    return "Hello world DevOps!"

# The webhook adress for a git account
@app.route("/github-webhook/", methods=["POST"])
def webhook():
    popup_text = "Un rédacteur vient de pousser du contenu sur GitHub"    
    data = json.loads(request.data)   
    redacteur = databaseSrv.get_redacteur_data(data['repository']['clone_url'], data['ref'])[0]
    # TODO - cas non trouve
    blocks = messagingSrv.format_slack_message(data['commits'][0]['author']['name'], redacteur)    
    gitSrv.clone(redacteur['gitAdress'], redacteur['gitBranchName'], redacteur['gitBranch'])
    converterSrv.convert()  
    cloudSrv.push() 
    messagingSrv.post_message_to_slack(redacteur['slackToken'].strip('"'), redacteur['slackChannel'].strip('"'), popup_text, blocks)
    return "Done"
   
    

@app.route("/enzo", methods=["GET"])
def enzo():
    # TODO - remove tmp file after method
    # gitSrv.clone("https://github.com/Groupe2filRouge/ProjetFilRouge.git")

    lien = databaseSrv.get_redacteur_data("https://github.com/EnzoPAGANO/mdfiles.git", "/ref/main")  
    print(lien)

    # converterSrv.convert()
    # cloudSrv.push()
    return "Done"

# The test adress for slack
@app.route("/testSlack", methods=["GET"])
def testSlack():
    return messagingSrv.testSlack();	

# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run(host= '0.0.0.0')
