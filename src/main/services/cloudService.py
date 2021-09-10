import boto3
import os
import json
import base64
import hashlib
import shutil

# The service for cloud operations
class CloudService():

    # Constructor
    def __init__(self):
        print("init CloudService")
        self.s3_client = boto3.client('s3')
        #Création du bucket à la volée:
        bucket_name="test-site-enzo"
        #self.s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'eu-west-3'}) #commentée pour éviter d'avoir à supprimer le bucket à chaque fois.
        website_configuration = {'IndexDocument': {'Suffix': 'README.html'}}
        self.s3_client.put_bucket_website(Bucket=bucket_name, WebsiteConfiguration=website_configuration)
        bucket_policy = {'Version': '2012-10-17','Statement': [{'Sid': 'AddPerm','Effect': 'Allow','Principal': '*','Action': ['s3:GetObject'],'Resource': "arn:aws:s3:::%s/*" % bucket_name}]}
        bucket_policy = json.dumps(bucket_policy)
        self.s3_client.put_bucket_policy(Bucket="test-site-enzo", Policy=bucket_policy)
        

    # Push from local file to cloud storage
    #def push(self, bucket): #argument bucket sera utile quand on aura la BDD
    def push(self):
        destination=""
        bucket="test-site-enzo"
        path="/tmp/converter"
        
        # Du code copié d'Internet, je ne saurais pas vraiment expliquer comment ça marche ¯\_(ツ)_/¯ 
        for root, dirs, files in os.walk(path):

            for filename in files:
                # construct the full local path
                local_path = os.path.join(root, filename)

                # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, path)
                s3_path = os.path.join(destination, relative_path)

                try:
                    self.s3_client.head_object(Bucket=bucket, Key=s3_path)
                except:
                    data=open(local_path,"rb")
                    #self.s3_client.upload_fileobj(data, bucket, s3_path, ExtraArgs={'ACL': 'public-read','Metadata': {'Content-Type': 'text/html'}})
                    self.s3_client.put_object(Key=s3_path,Body=data,Bucket=bucket,ContentType='text/html;charset=utf-8') #modifié : body=data et Key=s3_path et ContentType='text/html;charset=utf-8'
                    data.close() #test pour supprimer les erreurs au nettoyage, marche pas.
        
        #suppression du contenu du dossier temporaire
        html_tmp="/tmp/converter"
        #clone_tmp="/home/vagrant/tmp/clone"
        #try:
        #    shutil.rmtree(clone_tmp)
        #except OSError as erreur:
        #    print(f'Error: {clone_tmp} : {erreur.strerror}')
        #try:
        #    shutil.rmtree(html_tmp)
        #except OSError as erreur:
        #    print(f'Error: {html_tmp} : {erreur.strerror}')    #retourne toujours une erreur "text file busy", impossible de nettoyer le contenu html
        return "file uploaded"