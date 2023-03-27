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
    path = os.path.join(downloads, 's1ac_27th')
    temp = set()
    for fil in os.listdir(path):
        fil = fil.split("_")[0]
        temp.add(fil)
    temp = list(temp)
    print(len(temp))
    temp1 = temp[:100]
    temp2 = temp[100:200]
    temp3 = temp[200:]
    dest = os.path.join(downloads, 'hehe')
    for i in temp2:
        paths = glob(f"{path}/{i}*")
        print(paths)
        for j in paths:
            shutil.copy(j, dest)


copy_from_one_folder_to_another()
