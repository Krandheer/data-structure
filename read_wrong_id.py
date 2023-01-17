import pandas as pd
from datetime import datetime
import json

# json_file = {
#     "filesToProcess": []
# }
# path = "~/Downloads/Writer_Mongo_Data_Report_2023-01-16_2023-01-16T13_11_23.969Z.csv"
# df = pd.read_csv(path, low_memory=False)
# atm_id = df[(df['ALL_FILE_PASS'] == "False")]['ATMID']
# atm_id = atm_id[atm_id.str[:4] == 'S1CN']
#
#
# for ids in atm_id:
#     if ids == "dummy":
#         continue
#     json_file["filesToProcess"].append(ids)
#
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
# with open('bug_fail.json', 'w') as f:
#     json.dump(json_file, f)


path = "~/Downloads/Writer_Mongo_Data_Report_2023-01-11_2023-01-11T19_30_00.260Z.csv"
df = pd.read_csv(path, low_memory=False)


atm_ids = ['S1AC', 'S1BW', 'S1AW', 'S1BB', 'S1CN', 'S1NW', 'S1NB', 'MPB0']
result = {}
for ids in atm_ids:
    temp_df = df[df.ATMID.str[:4] == ids]
    df_1 = temp_df[((temp_df['CA-FILE_PASS'] == "True") & (temp_df['CB-FILE_PASS'] == "True")) & (
            (temp_df['SA-FILE_PASS'] == "False") | (temp_df['SB-FILE_PASS'] == "False"))]
    df_2 = temp_df[((temp_df['CA-FILE_PASS'] == "True") | (temp_df['CB-FILE_PASS'] == "True")) & (
            (temp_df['SA-FILE_PASS'] == "False") & (temp_df['SB-FILE_PASS'] == "False"))]

    atm_id_sa_sb = []
    atm_id_ca_cb = []
    for i in df_1['ATMID']:
        atm_id_sa_sb.append(i)
    for i in df_2['ATMID']:
        atm_id_ca_cb.append(i)

    result[f"{ids}_sa_sb"] = atm_id_sa_sb
    result[f"{ids}_ca_cb"] = atm_id_ca_cb

for key, val in result.items():
    print(key, len(val), val)

# df = df[df.ATMID.str[:4] == "S1BB"]
# df = df[((df['CA-FILE_PASS'] == "True") & (df['CB-FILE_PASS'] == "True")) & (
#         (df['SA-FILE_PASS'] == "False") | (df['SB-FILE_PASS'] == "False"))]
# atm_id = []
# df2 = df[['ATMID']]
# df2.to_csv('s1bb.csv', index=False)
# for ids in df["ATMID"]:
#     atm_ids.append(ids)
#
# print(len(atm_ids), atm_ids)
