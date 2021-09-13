import pymongo
from bson.json_util import dumps, loads
import random
import json
import logging

log = logging.getLogger(__name__)
# The service for database's operations
class DatabaseService():
    # Constructor
    def __init__(self):
        print("init DatabaseService")
        # local
        # pymongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
        # Docker
        myclient = pymongo.MongoClient("mongodb://root:secret@mongo")
        base_de_donnees = pymongoClient["projet"]
        self.redacteurs = base_de_donnees["liens"]
           
    # Getter for redactor data
    def get_redacteur_data(self, git, branch_ref):
        branch_name = branch_ref.split("/")[-1]
        query = { "gitAdress": git, "gitBranchName": branch_name}
        redacteur = list(self.redacteurs.find(query))
        return redacteur
