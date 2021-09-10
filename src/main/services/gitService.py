import subprocess
import os

# The service for git operations
class GitService():

    # Constructor
    def __init__(self):
        print('init GitService')

    # Clone repository from a given adress
    def clone(self, adresse):
        #subprocess.Popen(['git', 'clone', str(adresse), '~/tmp/clone'])
        #subprocess.Popen(['git', 'checkout', 'fil-28'])
        #Tests pour le changement de branche afin de créer des arborescences à convertir sans polluer la master:
        os.system('git'+' clone '+str(adresse)+' /tmp/clone')  #clone le git
        #os.chdir(r'~/tmp/clone') #change de dossier pour le checkout
        #os.system('git'+' checkout '+'fil-28') #se met dans ma branche pour tester
        return "git cloned"
