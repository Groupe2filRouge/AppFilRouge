import pymongo
from bson.json_util import dumps, loads
import random
import json

# The service for database's operations
class DatabaseService():
    
    # Constructor
    def __init__(self):
        print("init DatabaseService")
        pymongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
        base_de_donnees = pymongoClient["nom_base_de_donnees"]
        self.table = base_de_donnees["nom_de_table"]
