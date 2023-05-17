import json
import os
import csv

home = os.path.expanduser("~")
downloads = os.path.join(home, "Downloads")
path = os.path.join(downloads, 'hdfc_fail.json')

with open('hdfc_auth_fail_28th_feb.json', 'r') as f:
    data = json.load(f)

data = data['filesToProcess']

with open('hdfc_auth_28th_feb_analysis.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ATMID'])
    # Loop through the list of data and append each item to a new row in the CSV file
    for item in data:
        writer.writerow([item])
