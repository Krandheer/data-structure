import os

import pandas as pd
from datetime import datetime
import json


def get_wrong_id_json_file():
    json_file = {
        "filesToProcess": []
    }
    path = "~/Downloads/Writer_Mongo_Data_Report_2023-03-27_2023-03-27T19_30_00.981Z.csv"
    df = pd.read_csv(path, low_memory=False)
    atm_id = df[(df['ALL_FILE_PASS'] == "False")]['ATMID']

    # with open('.json', 'r') as f:
    #     canara_id = json.load(f)
    #
    # canara_ids = canara_id['filesToProcess']
    # for ids in atm_id:
    #     if ids in canara_ids:
    #         json_file['filesToProcess'].append(ids)
    atm_id = atm_id[atm_id.str[:4] == 'T1NS']
    # with open('india1_icici_atmid.json', 'r') as f:
    #     data = json.load(f)
    # data_id = data['atmid']
    temp = 0
    for ids in atm_id:
        if ids == 'dummy':
            continue
        if temp == 35:
            break
        json_file["filesToProcess"].append(ids)
        temp = temp+1

    paths = path.split("_")
    date_string = paths[4]
    date = datetime.strptime(date_string, '%Y-%m-%d')
    formatted_date = date.strftime('%m-%d-%Y')
    timestamp = int(date.timestamp())

    json_file['date'] = formatted_date
    json_file['updatedAt'] = timestamp

    with open('t1ns_fail.json', 'w') as f:
        json.dump(json_file, f)


get_wrong_id_json_file()


def get_top_fails():
    path = '~/Downloads/Writer_Mongo_Data_Report_2023-03-27_2023-03-27T19_30_00.981Z.csv'
    df = pd.read_csv(path, low_memory=False)
    df['prefix_atmid'] = df['ATMID'].str[:4]
    grouped = df.groupby(['prefix_atmid', 'ALL_FILE_PASS'])
    count = grouped.size().sort_values(ascending=False)
    for item in count.iteritems():
        if item[0][-1] == 'False':
            print(item)


# get_top_fails()
# path = "~/Downloads/Writer_Mongo_Data_Report_2023-02-21_2023-02-21T19_30_00.398Z.csv"
# df = pd.read_csv(path, low_memory=False)
#
#
# atm_ids = ['S1AC', 'S1BW', 'S1AW', 'S1BB', 'S1CN', 'S1NW', 'S1NB', 'MPB0']
# result = {}
# for ids in atm_ids:
#     temp_df = df[df.ATMID.str[:4] == ids]
#     df_1 = temp_df[((temp_df['CA-FILE_PASS'] == "True") & (temp_df['CB-FILE_PASS'] == "True")) & (
#             (temp_df['SA-FILE_PASS'] == "False") | (temp_df['SB-FILE_PASS'] == "False"))]
#     df_2 = temp_df[((temp_df['CA-FILE_PASS'] == "True") | (temp_df['CB-FILE_PASS'] == "True")) & (
#             (temp_df['SA-FILE_PASS'] == "False") & (temp_df['SB-FILE_PASS'] == "False"))]
#
#     atm_id_sa_sb = []
#     atm_id_ca_cb = []
#     for i in df_1['ATMID']:
#         atm_id_sa_sb.append(i)
#     for i in df_2['ATMID']:
#         atm_id_ca_cb.append(i)
#
#     result[f"{ids}_sa_sb"] = atm_id_sa_sb
#     result[f"{ids}_ca_cb"] = atm_id_ca_cb
#
# for key, val in result.items():
#     print(key, len(val))

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


def get_all_ids_of_bank(bank_name):
    downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    map_path = os.path.join(downloads, 'ATMID_BANKNAME_Details.csv')
    df = pd.read_csv(map_path)
    bank_ids_list = []
    bank_id = df[df['BankName'] == bank_name]['ATMID']
    for i in bank_id:
        if i not in bank_ids_list:
            bank_ids_list.append(i)
    json_file = {
        "filesToProcess": bank_ids_list
    }
    with open(f"{bank_name}.json", 'w') as f:
        json.dump(json_file, f)


# get_all_ids_of_bank("KOTAK MAHINDRA")
