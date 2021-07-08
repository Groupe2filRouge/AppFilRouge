import subprocess

# The service for git operations
class GitService():

    # Constructor
    def __init__(self):
        print('init GitService')

    # Clone repository from a given adress
    def clone(self, adresse):
        subprocess.Popen(['git', 'clone', str(adresse), '/home/vagrant/tmp/clone'])
        return "git cloned"
