import re
from AmazonScraper import AmazonScraper
from GoogleApi import GoogleSheetReader

# The ID and range of a sample spreadsheet.
CLIENT_SECRETS = '/home/leo/Desktop/google_credentials.json'
SPREADSHEET_ID = '1wJcG-DtL8Ba36jzcF6rtI2_csrsfm0wSbhSqo1CHFyg'
RANGE_NAME = 'TrackingInput!A2:B'

reader = GoogleSheetReader(SPREADSHEET_ID, RANGE_NAME, CLIENT_SECRETS)
trackingInputs = reader.getValues()

amazonScraper = AmazonScraper()

emailContent = []

for input in trackingInputs:
    Asin = input[0]
    OriginalPrice = float(input[1])
    output = {}
    try:
        productDetail = amazonScraper.AmzonParser(Asin)
        if float(productDetail['SALE_PRICE'].replace('$','')) - OriginalPrice < 1:
            output['productDetail'] = productDetail
            output['OriginalPrice'] = OriginalPrice

            emailContent.append(output)
    except Exception as e:
        pass

if len(emailContent) >=1 :
    print(emailContent)