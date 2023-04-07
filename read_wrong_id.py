import os

import pandas as pd
from datetime import datetime
import json


def get_wrong_id_json_file():
    json_file = {
        "filesToProcess": []
    }
    path = '~/Downloads/Writer_Mongo_Data_Report_2023-04-06_2023-04-06T19_30_00.905Z.csv'
    # path2 = "~/Downloads/OCRReport.csv"
    # df = pd.read_csv(path2, low_memory=False)
    # atm_id = df[(df['OCRAuthstatus'] == "Not Auth")]['ATMID']
    df = pd.read_csv(path, low_memory=False)
    atm_id = df[df["ALL_FILE_PASS"] == "False"]["ATMID"]
    with open('atmid/hdfc_ids.json', 'r') as f:
         data = json.load(f)

    hdfc_ids = data['filesToProcess']
    # for ids in ids:
    #     if ids in canara_ids:
    #         json_file['filesToProcess'].append(ids)
    # atm_id = atm_id[atm_id.str[:2] == 'MP']
    # with open('india1_icici.json', 'r') as f:
    #     data = json.load(f)
    # data_id = data['atmid']
    temp = 0
    for ids in atm_id:
        if ids == 'dummy':
            continue
        elif ids in hdfc_ids:
            json_file["filesToProcess"].append(ids)

    paths = path.split("_")
    date_string = paths[4]
    date = datetime.strptime(date_string, '%Y-%m-%d')
    formatted_date = date.strftime('%m-%d-%Y')
    timestamp = int(date.timestamp())

    json_file['date'] = formatted_date
    json_file['updatedAt'] = timestamp

    with open('hdfc_fail.json', 'w') as f:
        json.dump(json_file, f)


get_wrong_id_json_file()


def get_top_fails():
    path = '~/Downloads/Writer_Mongo_Data_Report_2023-04-06_2023-04-06T19_30_00.905Z'
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
    with open(f"{bank_name.lower()}.json", 'w') as f:
        json.dump(json_file, f)


# get_all_ids_of_bank("INDICASH-YES")

def get_auth_not_auth(bank_json_name):
    path = "~/Downloads/6OCRReport.csv"
    df = pd.read_csv(path)
    with open(f'atmid/{bank_json_name}.json', 'r') as f:
        data = json.load(f)
    data = data['filesToProcess']
    auth = []
    not_auth = []
    for i in df['ATMID']:
        if i in data and df[(df["ATMID"] == i) & (df["OCRAuthstatus"] == "Auth")]['OCRAuthstatus'].any() \
                and i not in auth:
            auth.append(i)
        elif i in data and not df[(df["ATMID"] == i) & (df["OCRAuthstatus"] == "Auth")]['OCRAuthstatus'].any() \
                and i not in not_auth:
            not_auth.append(i)
    with open(f'auth_fail/{bank_json_name}_29th_auth_fail.json', 'w') as f:
        json.dump({'atmid': not_auth}, f)
    print(bank_json_name, len(auth), len(not_auth))


# bank_name = ['hdfc_ids', 'icici', 'canara', 'axis', 'karur_vyas_bank', 'sbi', 'pnb', 'bob', 'indicash_axis',
#              'mon_spot_axis', 'indicash_yes', 'citi_atmid', 'india1_icici']
# for name in bank_name:
# get_auth_not_auth('hdfc_ids')

def auth_json():
    with open('auth_fail/hdfc_ids_6th_auth_fail.json', 'r') as f:
        data = json.load(f)
    data = data['atmid']
    date_string = '2023-04-06'
    date = datetime.strptime(date_string, '%Y-%m-%d')
    formatted_date = date.strftime('%m-%d-%Y')
    timestamp = int(date.timestamp())
    json_file = {"filesToProcess": data, 'date': formatted_date, 'updatedAt': timestamp}
    with open('hdfc_auth_fail.json', 'w') as f:
        json.dump(json_file, f)

# auth_json()
