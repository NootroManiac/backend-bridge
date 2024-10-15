import os
import google.auth
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import time

client_secret_file = r"C:\Users\goofy\Desktop\gettingjizzy\client_secret_233570314150-v3bpf9svucmku6lvled29pnqiun459gf.apps.googleusercontent.com.json"

SCOPES = ['https://www.googleapis.com/auth/documents']

def authenticate_and_build_service():
    # Create an OAuth flow instance
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secret_file, SCOPES)
    #module.module.class.method
    #google_auth_oauthlib is a module used for integrating google auth(authentication for google) and oauthlib(method of authentication)
    #flow() collection of all of the different google auth flows (offshores oauth logic to something called oauth2session(class))
    #installedappflow is a specific class within flow that handles the oauth logic for applications that interact with google api's(pass it a flow instance)
    #from_client_secrets_file (args: pathway to client secret json, scopes ) returns flow 
    #why does a flow instance need to be created IDK
    
    
    # Run local server to handle the OAuth 2.0 authorization flow
    credentials = flow.run_local_server(port=0)
    #class.method
    #flow is a class that has a method called run_local_server and many other useful functions and stores information 
    """Run the flow using the server strategy.

        The server strategy instructs the user to open the authorization URL in
        their browser and will attempt to automatically open the URL for them.
        It will start a local web server to listen for the authorization
        response. Once authorization is complete the authorization server will
        redirect the user's browser to the local web server. The web server
        will get the authorization code from the response and shutdown. The
        code is then exchanged for a token."""

    # Build the Google Docs API service
    service = googleapiclient.discovery.build('docs', 'v1', credentials=credentials)
    #discovery: google docs api is listed under the api discovery service (so i am assuming that it a universal library for all api's that are labeled under the api discovery service)
    #build: returns A Resource object with methods for interacting with the service.
    return service

def create_google_doc(service):
    document = service.documents().create().execute()
    print(f"Created Document with ID: {document['documentId']}")
    return document['documentId']

service = authenticate_and_build_service()

#docs_id = create_google_doc(service)

#print(docs_id)
#TODO
#you communicate with the google docs api with http requests 
text = ""
document_id = "1W0BdIHgKaOglXXgYOqx5jpt3G42KwMS0ptjAaz7VqIg"
def input_text(document_id,service,text,index):
    request = [
        {
            'insertText': {
                'location': {
                    'index': index,
                },
                'text': text 
            }
        }
    ]
    service.documents().batchUpdate(documentId = document_id, body = {'requests' : request}).execute()
input_text(document_id,service,text,1)
def input_looped_text(document_id, service, text,index,num_loops):
    #garbage
    request = [
        {
            'insertText': {
                'location': {
                    'index': index,
                },
                'text': text 
            }
        }
    ]
    for x in range(num_loops):
        service.documents().batchUpdate(documentId = document_id, body = {'requests' : request}).execute()
        time.sleep(1.6)

input_looped_text(document_id,service,text, 1, 100)
#look into how to setup a main file and format project accordingly 
