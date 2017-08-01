from __future__ import print_function
import httplib2
import os
import json
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

# try:
#     import argparse
#     flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
# except ImportError:
flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'linkedindata'

iterator = 1

def get_details():
    lists = []
    singleList = []
    with open("profile_details.json") as f:
        data = f.read()
        jsondata = json.loads(data)
        print(len(jsondata))
        for i in range(len(jsondata)):
            singleList.append(jsondata[i]["name"])
            singleList.append(jsondata[i]["url"])
            singleList.append(jsondata[i]["title"])
            singleList.append(jsondata[i]["email"])
            lists.append(singleList)
            singleList = []
    return lists, len(lists)

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def updatevalues(valueList):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)
    
    global iterator
    iterator = iterator + 1
    spreadsheetId = '1O6E93S3netMnfh308PzKzo6wtiqW-xBurM9TdYbylpg'
    rangeName = 'Sheet1!A' + str(iterator) + ':D' + str(iterator)
    

    values =[ valueList ]

    body = {
  'values': values
    }
    
    result = service.spreadsheets().values().update(
    spreadsheetId=spreadsheetId, range=rangeName,
    valueInputOption="RAW", body=body).execute()


