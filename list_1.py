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

with open('writercorp_sbi_2023-06-08 00:00:00.json', 'r') as f:
    data = json.load(f)

atmid = data['filesToProcess']

for i in atmid:
    if i not in temp:
        to_check.append(i)

print(len(to_check))
print(to_check)

temp = [
        ]


"""these 14 ids are missing in new pnb denom mapping provided by writer pnb = ['A1110210', 'A1125610', 'A1178510', 
'A1191110', 'A1214810', 'A2124210', 'A2187110', 'DC308000', 'N2169400', 'N4585900', 'N6153000', 'N8150500', 
'N8308000', 'NB600100'] 

confusing_pnb = ['D1015310', 'D1038920', 'D1770400', 'D2585900', 'D3076100', 'D5623800', "D5762600", "D6084600", 
"D6149400", "D7060700", 'DA386900', ] 

more_confusing = ['10416601', ]
"""