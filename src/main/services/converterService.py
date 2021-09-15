import markdown
import os
from os import walk
import tempfile
import shutil
from markdown.extensions.toc import TocExtension

arborescence={} #pour accéder à l'arboscence depuis toutes les fonctions
# The service for convertion operations
class ConverterService():

    # Constructor
    def __init__(self):
        print("init ConverterService")

    def convert(self, projectName):
        return self.browse("/tmp/clone/"+projectName, projectName)

    # Convert local .md file to .html file 
    def convert2Html(self, folder, fileName, currentFolder, destinationFolder):
        #construit l'arborescence en mémoire
        if currentFolder in arborescence.keys():
            arborescence[currentFolder].append(fileName)
        else:
            arborescence[currentFolder]=[fileName]
        print(arborescence)

        chemin=folder+"/"+fileName
        print("le chemin avant conversion :" + chemin)
        #lecture du fichier *.md
        with open(chemin, 'r') as f:
            text = f.read()
            html = markdown.markdown(text, extensions=['toc'])
#permet de créer le nom du fichier html à partir du nom d'origine
        fichierHTML=destinationFolder+currentFolder+"/"+fileName[:len(fileName)-3]+".html"
        #permet de créer le chemin de destination en miroir à l'arborescence d'origine
        destination=destinationFolder+currentFolder
        #écrit les fichiers convertis si l'arborescence miroire existe, crée l'arborescence sinon.
        if(os.path.exists(destination)):
            with open(fichierHTML, 'w') as f:
                f.write(html)
        else:
            os.makedirs(destination)
            with open(fichierHTML, 'w') as f:
                f.write(html)

        return "document converted"
    
    #Fonction pour faire un arbre déroulant avec l'arborescence des fichiers
    def ajoutArbre(self, destinationFolder, currentFolder, f, repertoire):
    #partie pour le tree view:
        fichierHTML=destinationFolder+currentFolder+"/"+f[:len(f)-3]+".html"
        #print(arborescence)
        arbo_html="<ul>"
        for dossier in arborescence.keys():
            arbo_html+="<li>"+dossier+"<ul>"
            for fichier in arborescence.get(dossier):
                #calcul du chemin relatif des fihiers pour les URL
                HTML=destinationFolder+dossier+"/"+fichier[:len(fichier)-3]+".html" #pour reconstruire les noms de fichiers
                cheminRelatif=os.path.relpath(HTML, destinationFolder+currentFolder)
                arbo_html+="<li> <a href=\""+cheminRelatif+"\">"+fichier[:len(fichier)-3]+"</a></li>" #modifier "fichier" en le chemin relatif des pages HTML pour les URL
            arbo_html+="</ul></li>"
        arbo_html+="</ul>"
        
        
        fichier = open(fichierHTML, "r")
        total = arbo_html + fichier.read()
        fichier.close()
        fichier = open(fichierHTML, "w")
        fichier.write(total)
        fichier.close()
        #print(arbo_html)

    def browse(self, folder, projectName):
            #si le dossier de destination n'existe pas :
        destinationFolder = "/tmp/converter/" + projectName
        if(not os.path.exists(destinationFolder)):
            os.makedirs(destinationFolder)
                
        for (repertoire, sousRepertoires, fichiers) in walk(folder):
            #ignore les dossiers cachés
            if(repertoire.find('.')==0):
                break
            for f in fichiers:
                # Si on a un ".md" alors on convertit
                if(f.find(".md") != -1):
                    # Compute current folder where f is 
                    currentFolder = repertoire[len(folder) : len(repertoire)]  #retiré le  - 1 après le premier folder
                    self.convert2Html(repertoire, f, currentFolder, destinationFolder)
        for (repertoire, sousRepertoires, fichiers) in walk(folder):
            #ignore les dossiers cachés
            if(repertoire.find('.')==0):
                break
            for f in fichiers:
                # Si on a un ".md" alors on convertit
                if(f.find(".md") != -1):
                    # Compute current folder where f is 
                    currentFolder = repertoire[len(folder) : len(repertoire)]  #retiré le  - 1 après le premier folder
                    self.ajoutArbre(destinationFolder, currentFolder, f, repertoire)

        return "Done"
    
def fonction_a_tester(self, param1, param2):
    return param1 + param2


