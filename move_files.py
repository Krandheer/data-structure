import csv
import os
from glob import glob

import pandas as pd
import json
import shutil

base_dir = os.path.expanduser('~')

downloads = os.path.join(base_dir, 'Downloads')


# path_hdfc = os.path.join(downloads, 'hdfc.csv')
# destination = os.path.join(downloads, 'hdfc')
# df = pd.read_csv(path_hdfc)
# atm_ids = []
# for item in df['ATMID']:
#     atm_ids.append(item)


def move(src, desti):
    files_to_move = glob(f'{src}/{id}*')
    for temp in files_to_move:
        shutil.copy(temp, desti)


# here folder is destination
def move_to_folder(folder):
    for id in atm_ids:
        if 'S1AC' in id:
            source = os.path.join(downloads, 'chunk_28_1')
            move(source, folder)

        elif 'S1AW' in id:
            source = os.path.join(downloads, 's1aw')
            move(source, folder)

        elif 'S1AN' in id:
            source = os.path.join(downloads, 'chunk_1')
            move(source, folder)


def create_json():
    with open(f'{downloads}/hdfc.json', 'w') as f:
        json.dump({'hdfc': atm_ids}, f)


def create_folder_inside_folder():
    hdfc_reports = os.path.join(downloads, 'hdfc_reports')
    for ids in atm_ids:
        os.makedirs(f'{hdfc_reports}/{ids}', exist_ok=True)


def file_inside_folder():
    hdfc_reports = os.path.join(downloads, 'hdfc_reports')
    os.listdir(hdfc_reports)


def copy_from_one_folder_to_another():
    path = os.path.join(downloads, 'axis_11th_may_auth')
    temp = set()
    for i in os.listdir(path):
        i = i.split("_")[0]
        temp.add(i)
    temp = list(temp)
    print(len(temp))

    temp = ["AECN02313", "AECN42813", "APCN09714", "APCN19226", "APCN29019", "APCN38817",
            "BECN115602", "BECN122406", "BECN137211", "BECN176601", "BECN210210", "BECN210211",
            "BECN310101", "BPCN133702", "BPCN169405", "BPCN171021", "BPCN192205",
            "BPCN196318", "BPCN196322", "BPCN201202", "BPCN201205", "BPCN213305", "BPCN255503", "BPCN280902",
            "BPCN286109", "BPCN317302", "CECN11125", "CECN42822", "CECN42824", "CECN48608", "CECN60528",
            "CPCN02114", "CPCN11122", "CPCN16117", "CPCN25939", "CPCN44907", "CPCN45908", "CPCN78925", "DECN105326",
            "DECN118124", "DECN219613", "DECN220131", "DECN249417", "DECN333102", "DECN348401",
            "DECN351902", "DECN373801", "DECN388101", "DECN394001", "DECN404901", "DECN414001", "DPCN104424",
            "DPCN144015", "DPCN191108", "DPCN204603", "DPCN255504", "DPCN289102", "SPAN28719", "SPAN28730",
            "SPCN28905", "TPCN122903", "TPCN13644", "TPCN13884", "TPCN155005", "TPCN155006", "TPCN16061",
            "TPCN169104", "TPCN270205", "TPCN300804", "TPCN10531", "SPCN8486", "BECN118222"]

    dest1 = os.path.join(downloads, 'axis_auth')

    # dest2 = os.path.join(downloads, '19th_hdfc_extraction')
    for i in temp:
        paths = glob(f"{path}/{i}*")
        print(paths)
        for j in paths:
            shutil.copy(j, dest1)
    # for i in temp2:
    #     paths = glob(f"{path}/{i}*")
    #     # print(paths)
    #     for j in paths:
    #         shutil.copy(j, dest2)
    #
    # for i in temp3:
    #     paths = glob(f"{path}/{i}*")
    #     # print(paths)
    #     for j in paths:
    #         shutil.copy(j, dest3)


copy_from_one_folder_to_another()


def another2():
    path = os.path.join(downloads, 'hdfc_auth_29th_april')
    path_csv = os.path.join(downloads, "hdfc probable pair correction - Sheet2.csv")
    df = pd.read_csv(path_csv)
    csv_temp = []
    for i in df["ATMID"]:
        if i not in csv_temp:
            csv_temp.append(i)
    folder_temp = []
    for i in os.listdir(path):
        i = i.split("_")[0]
        if i not in folder_temp:
            folder_temp.append(i)
    for i in folder_temp:
        if i not in csv_temp:
            paths = glob(f"{path}/{i}*")
            for j in paths:
                os.remove(j)
    # print(len(csv_temp), len(folder_temp))
    # dest = os.path.join(downloads, 'probable_pair')
    # for i in temp:
    #     paths = glob(f"{path}/{i}*")
    #     print(paths)
    #     for j in paths:
    #         shutil.copy(j, dest)

# another2()
