#https://developers.google.com/sheets/api/quickstart/python
# https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

class GoogleSheetReader:
    def __init__(self, spreadSheetId, rangeName, clientsecrets):
        self.spreadSheetId = spreadSheetId
        self.rangeName = rangeName
        self.clientsecrets = clientsecrets

    def getValues(self):
        """Shows basic usage of the Sheets API.
            Prints values from a sample spreadsheet.
            """
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(self.clientsecrets, SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('sheets', 'v4', http=creds.authorize(Http()))

        # Call the Sheets API
        result = service.spreadsheets().values().get(spreadsheetId=self.spreadSheetId,
                                                     range=self.rangeName).execute()
        return result.get('values', [])