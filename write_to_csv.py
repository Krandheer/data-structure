import json
import os
import csv

home = os.path.expanduser("~")
downloads = os.path.join(home, "Downloads")
path = os.path.join(downloads, 'writercorp_107.json')

# with open(path, 'r') as f:
#     data = json.load(f)

# data = data['filesToProcess']
# this is for 8th june sbi id, which is stuck at this level, once done then need prepare json and get the data
data = ['S1BW060047018', 'S1BB000104096', 'S1BW000048006', 'S1NW000048040', 'S1BG008851010', 'DFBK002013021', 'S1BB000083046', 'GFNH000262010', 'T1BY015077080', 'S1NW000146012', 'S1BW005626052', 'S1NW070094015', 'S1BW000196051', 'S1BB070120009', 'S1BW007252028', 'S1BB070120019', 'S1BW005626029', 'S1BW000300237', 'T1BY015077102', 'S1NB001891130', 'S1NW007252037', 'S1BB000399015', 'S1NB000571013', 'S1BB003030462', 'S1BG000938014', 'S1BW070094004', 'T1BY015077082', 'S1BB001355047', 'S1BW070120012', 'S1BW000104010', 'S1BB000083001', 'S1BB005922118', 'S1NW000195011', 'GFBH005560016', 'S1NB001684053', 'T1BF001377072', 'S1BB000947021', 'T1BH000300397', 'S1BG008851003', 'S1NB000399034', 'GFBH005560015', 'S1BW000048066', 'S1BW007074004', 'S1BB000196135', 'S1NB070094013', 'S1NG000300326', 'DFBK002013016', 'S1BB000346024', 'S1BG013538005', 'T1BY000181273', 'T1NH008851069', 'S1BB000395037', 'S1NB006240140', 'S1BB006240040', 'S1BB008851081', 'DFNK001171046', 'DFNK002024018', 'S1NC070094017', 'T1NY070094024', 'S1B2000835006', 'S1BG000947020', 'S1BW070103019', 'S1NB070103003', 'GFBH005560021']
with open('sample.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ATMID'])
    # Loop through the list of data and append each item to a new row in the CSV file
    for item in data:
        writer.writerow([item])

