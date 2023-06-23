import os

import pandas as pd
from datetime import datetime
import json


def get_wrong_id_json_file():
    path = '~/Downloads/Writer_Mongo_Data_Report_2023-06-22_2023-06-22T19_30_00.477Z.csv'
    # path = "~/Downloads/hdfc_400.csv"
    json_file = {
        "filesToProcess": []
    }

    df = pd.read_csv(path, low_memory=False)
    # atm_id = df[df["ALL_FILE_PASS"] == "False"]["ATMID"]
    atm_id = df["ATMID"]
    # atm_id = df["ATMID"]
    # with open('atmid/sbi.json', 'r') as f:
    #     data = json.load(f)
    #
    # hdfc = data['filesToProcess']
    # temp_ids = []
    # for i in atm_id:
    #     if i == 'dummy':
    #         continue
    #     elif i in hdfc:
    #         temp_ids.append(i)

    temp_ids = []
    for i in atm_id:
        if i == "dummy":
            continue
        temp_ids.append(i)

    print(len(temp_ids))
    # atm_id = atm_id[atm_id.str[:2] == 'TA']
    temp1 = temp_ids[:1000]
    temp2 = temp_ids[1000:2000]
    temp3 = temp_ids[2000:3000]
    temp4 = temp_ids[3000:4000]
    temp5 = temp_ids[4000:5000]
    temp6 = temp_ids[5000:6000]
    temp7 = temp_ids[6000:7000]
    temp8 = temp_ids[7000:8000]
    temp9 = temp_ids[8000:9000]
    temp10 = temp_ids[9000:10000]
    temp11 = temp_ids[10000:]

    paths = path.split("_")
    date_string = paths[4]
    # date_string = '2023-05-01'
    date = datetime.strptime(date_string, '%Y-%m-%d')
    formatted_date = date.strftime('%m-%d-%Y')
    timestamp = int(date.timestamp())

    json_file['date'] = formatted_date
    json_file['updatedAt'] = timestamp
    # json_file['filesToProcess'] = temp_ids
    for i in range(1, 12):
        if i == 1:
            json_file['filesToProcess'] = temp1
        elif i == 2:
            json_file['filesToProcess'] = temp2
        elif i == 3:
            json_file['filesToProcess'] = temp3
        elif i == 4:
            json_file['filesToProcess'] = temp4
        elif i == 5:
            json_file['filesToProcess'] = temp5
        elif i == 6:
            json_file['filesToProcess'] = temp6
        elif i == 7:
            json_file['filesToProcess'] = temp7
        elif i == 8:
            json_file['filesToProcess'] = temp8
        elif i == 9:
            json_file['filesToProcess'] = temp9
        elif i == 10:
            json_file['filesToProcess'] = temp10
        elif i == 11:
            json_file['filesToProcess'] = temp11

        with open(f'writercopr_data{i}.json', 'w') as f:
            json.dump(json_file, f)


# get_wrong_id_json_file()


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
    with open("icici.json", 'r') as f:
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
    amygb_data = os.path.join(os.path.expanduser("~"), "Downloads")
    map_path = os.path.join(amygb_data, 'ATMID_BANKNAME_Details.csv')
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


# get_all_ids_of_bank("PNB")


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
    # path = "~/Downloads/11thmay_auth.csv"
    # with open('atmid/sbi.json', 'r') as f:
    #     data = json.load(f)
    # data = data['filesToProcess']
    # temp = []
    # df = pd.read_csv(path, low_memory=False)
    # atmids = df[df['OCRAuthstatus'] == 'Not Auth']['ATMID']
    # for i in atmids:
    #     if i in data and i not in temp:
    #         temp.append(i)
    temp = ["40228503", "40266002", "40351202", "40440502", "40447901", "40450101", "40527901", "40531913", "40551001",
            "40556401", "40565401", "40644903", "40690501", "40690601", "60108609", "60219407", "60246006", "60273901",
            "10346402", "40208010", "40269802", "40309502", "40309503", "40337704", "40337706", "40346401", "40349402",
            "40417501", "40483202", "40521001", "40521202", "40536801", "40546102", "40549201", "40550402", "40566001",
            "40566601", "40581603", "40589002", "40637201", "40637601", "40639802", "40677201", "40679001", "40693301",
            "60246004", "60246005", "60272201", "60456402", "70208003", ]
    print(len(temp))
    date_string = '2023-06-06'
    date = datetime.strptime(date_string, '%Y-%m-%d')
    formatted_date = date.strftime('%m-%d-%Y')
    timestamp = int(date.timestamp())
    json_file = {"filesToProcess": temp, 'date': formatted_date, 'updatedAt': timestamp}
    with open('india1_icici_5th_june.json', 'w') as f:
        json.dump(json_file, f)


# auth_json()

def get_fail_pass(bank_name):
    path = '~/Downloads/Writer_Mongo_Data_Report_2023-06-07_2023-06-07T19_30_00.221Z.csv'
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
    with open("hdfc_ids.json", 'r') as f:
        data = json.load(f)
    hdfc = data['filesToProcess']

    temp = 0
    for i in atm_id:
        if i in hdfc:
            temp += 1
    print(temp)


# total_of_particular_bank_processed_on_given_day()

def hdfc24th(bank_name):
    path = '~/Downloads/Writer_Mongo_Data_Report_2023-06-22_2023-06-22T19_30_00.477Z.csv'
    df = pd.read_csv(path, low_memory=False)
    atmid = df[df['ALL_FILE_PASS'] == 'False']['ATMID']
    atmid3 = df[(df['ALL_FILE_PASS'] == 'False') & (df["CA-FILE_PASS"] != "True") & (df["CB-FILE_PASS"] != "True")
                & (df["SA-FILE_PASS"] != "True") & (df["SB-FILE_PASS"] != "True")]['ATMID']
    with open(f'atmid/{bank_name}.json', 'r') as f:
        data = json.load(f)

    data = data['filesToProcess']

    temp = []
    temp1 = []
    for i in df['ATMID']:
        if i in data:
            temp1.append(i)
    for i in atmid:
        if i == "dummy":
            continue
        elif i in data and i not in temp:
            temp.append(i)
    temp2 = []
    for i in atmid3:
        if i in data and i not in temp2:
            temp2.append(i)
    # print(temp2)
    # temp_ids = []
    # for ids in atmid3:
    #     if ids not in temp_ids:
    #         temp_ids.append(ids)
    # temp3 = temp_ids[:1000]
    # temp4 = temp_ids[1000:]
    print(f"{bank_name}, total: {len(temp1)}, failed: {len(temp)}, all 4 failed {len(temp2)}")
    # paths = path.split("_")
    # date_string = paths[4]
    date_string = '2023-06-14'
    date = datetime.strptime(date_string, '%Y-%m-%d')
    formatted_date = date.strftime('%m-%d-%Y')
    # formatted date = month-date-year
    timestamp = int(date.timestamp())
    json_file = {'date': formatted_date, 'updatedAt': timestamp, 'filesToProcess': temp2}
    with open(f"writercorp_{bank_name}_{date}.json", 'w') as f:
        json.dump(json_file, f)


bank_names = ['sbi', 'hdfc', 'canara', 'icici', 'karur_vysya_bank', 'axis', 'pnb', 'cub', "idbi", 'india1-icici',
              'mon-spot-icici']


# bank_names = ['sbi', 'hdfc_ids', 'canara', 'icici', 'karur_vyas_bank', 'axis', 'cub', 'india1_icici',
# 'mon-spot-icici', 'pnb']
# for bank_name in bank_names:
#     hdfc24th(bank_name)

# hdfc24th()
# hdfc24th('sbi')


def get_top_fails():
    path = '~/Downloads/Writer_Mongo_DataExtended_Report_2023-06-16_2023-06-16T07_05_38.337Z.csv'
    path2 = '~/Downloads/ATMID_BANKNAME_Details.csv'
    df1 = pd.read_csv(path, low_memory=False)
    df2 = pd.read_csv(path2, low_memory=False)
    df3 = pd.merge(df2, df1, on="ATMID")
    grouped = df3.groupby(['BankName', 'ALL_FILE_PASS'])
    count = grouped.size().sort_values(ascending=False)
    for item in count.iteritems():
        if item[0][-1] == 'False':
            print(item)


# get_top_fails()
def all_4_fail():
    path = '~/Downloads/Writer_Mongo_Data_Report_2023-06-22_2023-06-22T19_30_00.477Z.csv'
    df = pd.read_csv(path, low_memory=False)
    atmid = df[df['ALL_FILE_PASS'] == 'False']['ATMID']
    atmid3 = df[(df['ALL_FILE_PASS'] == 'False') & (df["CA-FILE_PASS"] != "True") & (df["CB-FILE_PASS"] != "True")
                & (df["SA-FILE_PASS"] != "True") & (df["SB-FILE_PASS"] != "True")]['ATMID']

    temp = []
    count = 0
    for i in atmid3:
        count += 1
        if count > 100:
            break
        temp.append(i)

    paths = path.split("_")
    date_string = paths[4]
    # date_string = '2023-06-14'
    date = datetime.strptime(date_string, '%Y-%m-%d')
    formatted_date = date.strftime('%m-%d-%Y')
    # formatted date = month-date-year
    timestamp = int(date.timestamp())
    json_file = {'date': formatted_date, 'updatedAt': timestamp, 'filesToProcess': temp}
    with open(f"writercorp_{date}.json", 'w') as f:
        json.dump(json_file, f)


all_4_fail()
