import csv
import os
from glob import glob

import pandas as pd
import json
import shutil

base_dir = os.path.expanduser("~")

downloads = os.path.join(base_dir, "Downloads")


def move(src, desti):
    files_to_move = glob(f"{src}/{id}*")
    for temp in files_to_move:
        shutil.copy(temp, desti)


# here folder is destination
def move_to_folder(folder):
    for id in atm_ids:
        if "S1AC" in id:
            source = os.path.join(downloads, "chunk_28_1")
            move(source, folder)

        elif "S1AW" in id:
            source = os.path.join(downloads, "s1aw")
            move(source, folder)

        elif "S1AN" in id:
            source = os.path.join(downloads, "chunk_1")
            move(source, folder)


def create_json():
    with open(f"{downloads}/hdfc.json", "w") as f:
        json.dump({"hdfc": atm_ids}, f)


def create_folder_inside_folder():
    hdfc_reports = os.path.join(downloads, "hdfc_reports")
    for ids in atm_ids:
        os.makedirs(f"{hdfc_reports}/{ids}", exist_ok=True)


def file_inside_folder():
    hdfc_reports = os.path.join(downloads, "23rd_june_hdfc_auth")
    os.listdir(hdfc_reports)


def copy_from_one_folder_to_another():
    path = os.path.join(downloads, "3rd-july-axis-auth")

    temp = set()
    for ids in os.listdir(path):
        ids = ids.split("_")[0]
        temp.add(ids)

    temp = list(temp)
    temp1 = temp[:100]
    print(len(temp))

    dest1 = os.path.join(downloads, "3rd_july_axis_debug")
    # dest2 = os.path.join(downloads, "3rd_july_axis_debug")

    for i in temp1:
        paths = glob(f"{path}/{i}*")
        print(paths)
        for j in paths:
            shutil.copy(j, dest1)


copy_from_one_folder_to_another()


def another2():
    path = os.path.join(downloads, "hdfc_auth_29th_april")
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


# another2()
