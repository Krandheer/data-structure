import json

import pandas as pd

path = "~/Downloads/sbi_master_denom_corrected.csv"
path2 = "~/Downloads/sbi_master_not_correctable.csv"
df = pd.read_csv(path)
df2 = pd.read_csv(path2)
temp = []
for i in df['ATMID']:
    if i not in temp:
        temp.append(i)

for i in df2['ATMID']:
    if i not in temp:
        temp.append(i)
to_check = []

with open('writercorp_sbi_2023-06-07 00:00:00.json', 'r') as f:
    data = json.load(f)

atmid = data['filesToProcess']

for i in atmid:
    if i not in temp:
        to_check.append(i)

print(to_check)
