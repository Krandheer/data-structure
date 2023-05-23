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
    path = os.path.join(downloads, 'sbi_11th_may_chunk')
    temp = set()
    for i in os.listdir(path):
        i = i.split("_")[0]
        temp.add(i)
    temp = list(temp)
    print(len(temp))

    # temp1 = temp[:100]
    # temp2 = temp[100:]
    # temp3 = temp[200:]
    temp1 = ["S1BW000074016", "S1BW000074028", "S1BW000074086", "S1BW000093098", "S1BW000178007", "S1BW000178009",
             "S1BW000178012", "S1BW000178013", "S1BW000178072", "S1BW000178152", "S1BW000181017", "S1BW000181022",
             "S1BW000181036", "S1BW000181040", "S1BW000181047", "S1BW000181049", "S1BW000181140", "S1BW000181142",
             "S1BW000300037", "S1BW000300159", "S1BW000334010", "S1BW000432192", "S1BW000463005", "S1BW000835059",
             "S1BW000938005", "S1BW001490059", "S1NW001355015", "CFBA020018005", "CFBA020018015", "DBBK000196111",
             "DBBK000196115", "DFBK001171044", ]
    dest1 = os.path.join(downloads, 'sbi_11th_1')
    # dest2 = os.path.join(downloads, '19th_hdfc_extraction')
    for i in temp1:
        paths = glob(f"{path}/{i}*")
        print(paths)
        for j in paths:
            shutil.copy(j, dest1)
    # for i in temp2:
    #     paths = glob(f"{path}/{i}*")
    #     print(paths)
    #     for j in paths:
    #         shutil.copy(j, dest2)


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
