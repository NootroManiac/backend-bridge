import os
import google.auth
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

client_secret_file = r"C:\Users\goofy\Desktop\gettingjizzy\client_secret_233570314150-v3bpf9svucmku6lvled29pnqiun459gf.apps.googleusercontent.com.json"

SCOPES = ['https://www.googleapis.com/auth/documents']

def authenticate_and_build_service():
    # Create an OAuth flow instance
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secret_file, SCOPES)
    
    # Run local server to handle the OAuth 2.0 authorization flow
    credentials = flow.run_local_server(port=0)
    
    # Build the Google Docs API service
    service = googleapiclient.discovery.build('docs', 'v1', credentials=credentials)
    return service

def create_google_doc(service):
    document = service.documents().create().execute()
    print(f"Created Document with ID: {document['documentId']}")
    return document['documentId']

service = authenticate_and_build_service()

docs_id = create_google_doc(service)

print(docs_id)
#TODO
text = "hello"
def input_text(text):
    #garbage   
    x = 5
def input_looped_text(text, num_loops):
    #garbage
    x = 5
#look into how to setup a main file and format project accordingly 
