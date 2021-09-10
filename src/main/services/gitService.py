import subprocess
import os

# The service for git operations
class GitService():

    # Constructor
    def __init__(self):
        print('init GitService')

    # Clone repository from a given adress
    def clone(self, adress, branch, isBranch):
        #Tests pour le changement de branche afin de créer des arborescences à convertir sans polluer la master:
        os.system('git'+' clone '+str(adress)+' /tmp/clone')  #clone le git
        #if(isBranch)            
        #    os.chdir(r'~/tmp/clone') #change de dossier pour le checkout
        #    os.system('git'+' checkout '+ branch) #se met dans la branche
        return "git cloned"
