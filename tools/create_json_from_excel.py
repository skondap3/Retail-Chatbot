import csv
import json

dict = {
"Brand" : "Bella",
"Product" : "Steam Iron",
"Price": "19",
"url" : "www.google.com"
}

with open(r'C:\Users\IBM_ADMIN\Desktop\Chat_Bot\test_upload_text.json', 'w') as jsonfile:
    json.dump(dict, jsonfile)


print("complete")