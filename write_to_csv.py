import json
import os
import csv

home = os.path.expanduser("~")
downloads = os.path.join(home, "Downloads")
path = os.path.join(downloads, 'hdfc_auth_fail.json')

with open(path, 'r') as f:
    data = json.load(f)

data = data['filesToProcess']

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id'])
    # Loop through the list of data and append each item to a new row in the CSV file
    for item in data:
        writer.writerow([item])
