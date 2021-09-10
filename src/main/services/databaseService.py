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
        pymongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
        base_de_donnees = pymongoClient["projetFR"]
        self.redacteurs = base_de_donnees["redacteurs"]
           
    # Getter for redactor data
    def get_redacteur_data(self, git, branch_ref):
        branch_name = branch_ref.split("/")[-1]
        redacteur = list(self.redacteurs.find({ "gitAdress": git }, {"gitBranchName": branch_name}))
        #import pdb;pdb.set_trace()
        return redacteur
