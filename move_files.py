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
    path = os.path.join(downloads, '11th_axis_triangulation')
    temp = set()
    for i in os.listdir(path):
        i = i.split("_")[0]
        temp.add(i)
    temp = list(temp)
    print(len(temp))

    temp = ["CECN19236", "CECN19234", "CECN19240", "DECN438806", "DECN433301", "CECN19238", "CECN1923", "DECN105031",
            "BECN176615", "DECN111215", "APCN23108", "DECN300604", "DECN149835", "CECN43318", "DECN167419",
            "CECN19237", "BPCN141103", "DECN149831", "DECN171036", "CECN26532", "DECN149833", "DECN149834",
            "DECN396401", "DPCN192602", "DECN149832", "DECN477701", "DECN324006", "DECN165823", "CECN11133",
            "DECN372502", "DECN130441", "CECN11131", "SPCN29509", "DECN273817", "APCN59007", "DECN104439",
            "DECN201107", "DECN299406", "DECN367102", "DECN443701", "CECN57527", "AECN12510", "DECN273819",
            "DECN111936", "DECN273816", "APCN59008", "BECN146916", "DECN324112", "DECN314505", "DECN280803", ]

    dest1 = os.path.join(downloads, 'axis_triang')

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
