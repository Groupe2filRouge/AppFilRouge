import markdown
from os import walk

# The service for convertion operations
class ConverterService():

    # Constructor
    def __init__(self):
        print("init ConverterService")

    def convert(self):
        return self.browse("/home/vagrant/tmp/clone/")

    # Convert local .md file to .html file 
    def convert2Html(self, folder, fileName, currentFolder, destinationFolder):

        # mdFile = "full_name: {}".format(data['repository']['full_name'])
        # TODO - concat folder + filename
        with open('/home/vagrant/tmp/clone/README.md', 'r') as f:
            text = f.read()
            html = markdown.markdown(text)

        # TODO - concat destinationFolder + currentFolder + filename        
        # TODO - check if destinationFolder + currentFolder exists otherwise create...
        with open('/home/shared/converter/tmp/README.html', 'w') as f:
            f.write(html)

        return "document converted"

    def browse(self, folder):
        print('browse from ' + folder)
        destinationFolder = "..."
        # TODO - doit pouvoir servir pour la table des matieres...
        listeFichiers = []
        for (repertoire, sousRepertoires, fichiers) in walk(folder):
            print("+--- " + repertoire)
            # Si le repertoire contient ".xxx" alors on ignore => utiliser find
            # Sinon lister les fichiers. 
            for f in fichiers: 
                print("fichier: {}".format(f))                
                # Si on a un ".md" alors on convertit
                if(f.find(".md")):
                    # Compute current folder where f is 
                    currentFolder = repertoire[len(folder): len(repertoire)]
                    print("current folder: " + currentFolder)
                    self.convert2Html(repertoire, f, currentFolder, destinationFolder)
            
        return "Done"
