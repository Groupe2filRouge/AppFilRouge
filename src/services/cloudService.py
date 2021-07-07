import boto3

# The service for cloud operations
class CloudService():

    # Constructor
    def __init__(self):
        print("init CloudService")
        s3_client = boto3.client('s3')

    # Push from local file to cloud storage
    def push(self, bucket):
        s3_client.upload_file("/home/shared/tmp/README.html", "lebucketpythondalex", "keyfilename")
        return "file uploaded"