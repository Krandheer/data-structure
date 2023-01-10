import pandas as pd
from datetime import datetime
import json

# json_file = {
#     "filesToProcess": []
# }
# path = "~/Downloads/Writer_Mongo_Data_Report_2022-12-27_2022-12-27T19_30_00.249Z.csv"
# df = pd.read_csv(path, low_memory=False)
# atm_id = df[(df['ALL_FILE_PASS'] == "False")]['ATMID']
# atm_id = atm_id[atm_id.str[:4] == 'S1AC']
#
# for ids in atm_id:
#     if ids == "dummy":
#         continue
#     json_file["filesToProcess"].append(ids)
#
# paths = path.split("_")
# date_string = paths[4]
# date = datetime.strptime(date_string, '%Y-%m-%d')
# formatted_date = date.strftime('%m-%d-%Y')
# timestamp = int(date.timestamp())
#
# json_file['date'] = formatted_date
# json_file['updatedAt'] = timestamp
#
# with open('failed_cases.json', 'w') as f:
#     json.dump(json_file, f)


path = "~/Downloads/Writer_Mongo_Data_Report_2022-12-27_2022-12-27T19_30_00.249Z.csv"
df = pd.read_csv(path, low_memory=False)
df = df[((df['CA-FILE_PASS'] == "True") & (df['CB-FILE_PASS'] == "True")) & (
        (df['SA-FILE_PASS'] == "False") | (df['SB-FILE_PASS'] == "False"))]
df = df[df.ATMID.str[:4] == "S1AC"]
atm_ids = []
for ids in df["ATMID"]:
    atm_ids.append(ids)

print(len(atm_ids), atm_ids)
