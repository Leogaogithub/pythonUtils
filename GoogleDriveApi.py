#https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
import gspread
from oauth2client.service_account import ServiceAccountCredentials

trackingInputSheet = 'TrackingInput'
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/leo/Desktop/LeoSheet-c4a3c1c70b36.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
x = client.list_spreadsheet_files()
client.create('amazonPriceTracking1')
x = client.list_spreadsheet_files()


sheet = client.open('amazonPriceTracking1')#.worksheet(trackingInputSheet)

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)