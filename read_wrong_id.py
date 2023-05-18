import os

import pandas as pd
from datetime import datetime
import json


def get_wrong_id_json_file():
    path = '~/Downloads/Writer_Mongo_Data_Report_2023-04-24_2023-04-24T19_30_00.991Z.csv'
    json_file = {
        "filesToProcess": []
    }

    df = pd.read_csv(path, low_memory=False)
    # atm_id = df[df["ALL_FILE_PASS"] == "True"]["ATMID"]
    atm_id = df["ATMID"]
    with open('atmid/hdfc_ids.json', 'r') as f:
        data = json.load(f)

    hdfc = data['filesToProcess']
    temp_ids = []
    for i in atm_id:
        if i == 'dummy':
            continue
        elif i in hdfc:
            temp_ids.append(i)

    print(len(temp_ids))
    # atm_id = atm_id[atm_id.str[:2] == 'TA']
    temp1 = temp_ids[:1000]
    temp2 = temp_ids[1000:2000]
    temp3 = temp_ids[2000:3000]
    temp4 = temp_ids[3000:]

    # for ids in atm_id:
    #     if ids == 'dummy':
    #         continue
    #     elif ids in hdfc:
    #         json_file["filesToProcess"].append(ids)
    #

    paths = path.split("_")
    date_string = paths[4]
    date = datetime.strptime(date_string, '%Y-%m-%d')
    formatted_date = date.strftime('%m-%d-%Y')
    timestamp = int(date.timestamp())

    json_file['date'] = formatted_date
    json_file['updatedAt'] = timestamp

    for i in range(1, 5):
        if i == 1:
            json_file['filesToProcess'] = temp1
        elif i == 2:
            json_file['filesToProcess'] = temp2
        elif i == 3:
            json_file['filesToProcess'] = temp3
        elif i == 4:
            json_file['filesToProcess'] = temp4

        with open(f'writercorp_{i}.json', 'w') as f:
            json.dump(json_file, f)


# get_wrong_id_json_file()


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
def probable_pair_correction_ids():
    path = "~/Downloads/Writer_Mongo_Data_Report_2023-04-06_2023-04-06T19_30_00.905Z.csv"
    df = pd.read_csv(path, low_memory=False)
    df = df[df["ALL_FILE_PASS"] == "False"]
    df1 = df[
        (
                ((df['CA-FILE_PASS'] == "True") & (df['SA-FILE_PASS'] == "True")) |
                ((df['CA-FILE_PASS'] == "False") & (df['SA-FILE_PASS'] == "True")) |
                ((df['CA-FILE_PASS'] == "True") & (df['SA-FILE_PASS'] == "False"))
        ) &
        (
                ((df['SB-FILE_PASS'] == "False") & (df['CB-FILE_PASS'] == "True")) |
                ((df['SB-FILE_PASS'] == "True") & (df['CB-FILE_PASS'] == "False"))
        )
        ]
    df2 = df[
        (
                ((df['CB-FILE_PASS'] == "True") & (df['SB-FILE_PASS'] == "True")) |
                ((df['CB-FILE_PASS'] == "False") & (df['SB-FILE_PASS'] == "True")) |
                ((df['CB-FILE_PASS'] == "True") & (df['SB-FILE_PASS'] == "False"))
        ) &
        (
                ((df['SA-FILE_PASS'] == "False") & (df['CA-FILE_PASS'] == "True")) |
                ((df['SA-FILE_PASS'] == "True") & (df['CA-FILE_PASS'] == "False"))
        )
        ]
    with open("atmid/icici.json", 'r') as f:
        data = json.load(f)
    data = data['filesToProcess']
    temp = set()
    for i in df1['ATMID']:
        if i in data:
            temp.add(i)
    for i in df2['ATMID']:
        if i in data:
            temp.add(i)

    temp = list(temp)
    with open("icici_pair.json", 'w') as f:
        json.dump({'filesToProcess': temp}, f)


# probable_pair_correction_ids()


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
    path = "~/Downloads/11OCRReport.csv"
    df = pd.read_csv(path)
    with open(f'atmid/{bank_json_name}.json', 'r') as f:
        data = json.load(f)
    data = data['filesToProcess']
    auth = []
    not_auth = []
    temp = 0
    for i in df['ATMID']:
        if temp > 20:
            break
        if i in data and df[(df["ATMID"] == i) & (df["OCRAuthstatus"] == "Auth")]['OCRAuthstatus'].any() \
                and i not in auth:
            auth.append(i)
        elif i in data and not df[(df["ATMID"] == i) & (df["OCRAuthstatus"] == "Auth")]['OCRAuthstatus'].any() \
                and i not in not_auth:
            temp = temp + 1
            print(i)
            not_auth.append(i)
    with open(f'auth_fail/{bank_json_name}_auth_fail.json', 'w') as f:
        json.dump({'atmid': not_auth}, f)
    print(bank_json_name, len(auth), len(not_auth))


# bank_name = ['hdfc_ids', 'icici', 'canara', 'axis', 'karur_vyas_bank', 'sbi', 'pnb', 'bob', 'indicash_axis',
#              'mon_spot_axis', 'indicash_yes', 'citi_atmid', 'india1_icici']
# bank_name = ['hdfc_ids', 'icici']
# for name in bank_name:
# get_auth_not_auth('hdfc_ids')


def auth_json():
    path = "~/Downloads/11thmay_auth.csv"
    with open('atmid/icici.json', 'r') as f:
        data = json.load(f)
    data = data['filesToProcess']
    temp = []
    df = pd.read_csv(path, low_memory=False)
    atmids = df[df['OCRAuthstatus'] == 'Not Auth']['ATMID']
    for i in atmids:
        if i in data and i not in temp:
            temp.append(i)
    print(len(temp))
    date_string = '2023-05-11'
    date = datetime.strptime(date_string, '%Y-%m-%d')
    formatted_date = date.strftime('%m-%d-%Y')
    timestamp = int(date.timestamp())
    json_file = {"filesToProcess": temp, 'date': formatted_date, 'updatedAt': timestamp}
    with open('icici_auth_fail_11th_may.json', 'w') as f:
        json.dump(json_file, f)


auth_json()


# print("")

def get_fail_pass(bank_name):
    path = '~/Downloads/Writer_Mongo_Data_Report_2023-04-06_2023-04-06T19_30_00.905Z.csv'
    # path2 = "~/Downloads/OCRReport.csv"
    # df = pd.read_csv(path2, low_memory=False)
    # atm_id = df[(df['OCRAuthstatus'] == "Not Auth")]['ATMID']
    df = pd.read_csv(path, low_memory=False)
    atm_id = df[df["ALL_FILE_PASS"] == "False"]["ATMID"]
    atm_id2 = df[df["ALL_FILE_PASS"] == "True"]["ATMID"]
    atm_id = df["ATMID"]
    with open(f'atmid/{bank_name}.json', 'r') as f:
        data = json.load(f)

    temp_ids = data['filesToProcess']
    fail = []
    total = []
    for i in atm_id:
        if i == 'dummy':
            continue
        if i in temp_ids:
            total.append(i)
            if df[(df["ATMID"] == i) & (df["ALL_FILE_PASS"] == "False")]['ALL_FILE_PASS'].any():
                fail.append(i)
    print(len(total), len(fail))


# get_fail_pass('icici')

def total_of_particular_bank_processed_on_given_day():
    path = '~/Downloads/Writer_Mongo_Data_Report_2023-04-06_2023-04-06T19_30_00.905Z.csv'
    df = pd.read_csv(path, low_memory=False)
    atm_id = df['ATMID']
    with open("atmid/hdfc_ids.json", 'r') as f:
        data = json.load(f)
    hdfc = data['filesToProcess']

    temp = 0
    for i in atm_id:
        if i in hdfc:
            temp += 1
    print(temp)


# total_of_particular_bank_processed_on_given_day()

def hdfc24th():
    path = '~/Downloads/Writer_Mongo_Data_Report_2023-05-04_2023-05-04T19_30_00.448Z.csv'
    df = pd.read_csv(path, low_memory=False)
    atmid = df[df['ALL_FILE_PASS'] == 'False']['ATMID']
    atmid3 = df[(df['ALL_FILE_PASS'] == 'False') & (df["CA-FILE_PASS"] != "True") & (df["CB-FILE_PASS"] != "True")
                & (df["SA-FILE_PASS"] != "True") & (df["SB-FILE_PASS"] != "True")]['ATMID']
    atmid2 = df['ATMID']
    with open('atmid/hdfc_ids.json', 'r') as f:
        data = json.load(f)

    data = data['filesToProcess']

    temp = []
    for i in atmid:
        if i == "dummy":
            continue
        elif i in data and i not in temp:
            temp.append(i)
    temp2 = []
    for i in atmid2:
        if i == 'dummy':
            continue
        elif i in data and i not in temp2:
            temp2.append(i)
    temp3 = []
    for i in atmid3:
        if i in data and i not in temp3:
            temp3.append(i)
    print(temp3)
    print(len(temp), len(temp2), len(temp3))
    pas = df[df['ALL_FILE_PASS'] == 'True']["ATMID"]
    fai = df[df['ALL_FILE_PASS'] == 'False']["ATMID"]
    print(len(pas), len(fai))
    # json_file = {
    #     "filesToProcess": temp3
    # }
    # paths = path.split("_")
    # date_string = paths[4]
    # date = datetime.strptime(date_string, '%Y-%m-%d')
    # formatted_date = date.strftime('%m-%d-%Y')
    # timestamp = int(date.timestamp())
    #
    # json_file['date'] = formatted_date
    # json_file['updatedAt'] = timestamp
    #
    # with open("hdfc_29th_auth_fail.json", 'w') as f:
    #     json.dump(json_file, f)
    # 63.13 pass


# hdfc24th()

def check_in():
    with open('atmid/hdfc_ids.json', 'r') as f:
        data = json.load(f)
    hdfc_ids = data['filesToProcess']

    with open('ids_358.json', 'r') as f:
        data = json.load(f)

    in_hdfc = 0
    for i in data:
        if i not in hdfc_ids:
            in_hdfc += 1
