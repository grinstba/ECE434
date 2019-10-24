from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import time, sys

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1B1o1ZuExY96EVZBI55J4rkb1WMDuUXLTgqbvwaEe8MU'
RANGE_NAME = 'A2'

def main(temp):
    """Shows basic usage of the Sheets API.
    Writes values to a sample spreadsheet.
    """
    store = file.Storage('tokenPython.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    # Compute a timestamp and pass the first two arguments
    # values = [ [time.time()/60/60/24+ 25569 - 4/24, sys.argv[1], sys.argv[2]]]
    values = [ [time.time()/60/60/24+ 25569 - 4/24, temp]]
    body = { 'values': values }
    result = service.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID,
                            range=RANGE_NAME,
                            #  How the input data should be interpreted.
                            valueInputOption='USER_ENTERED',
                            # How the input data should be inserted.
                            # insertDataOption='INSERT_ROWS'
                            body=body
                            ).execute()
    
    updates = result.get('updates', [])
    # print(updates)

    if not updates:
        print('Not updated')

if __name__ == '__main__':
    main()