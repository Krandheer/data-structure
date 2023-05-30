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
    path = os.path.join(downloads, 'sbi_11th_may_chunk')
    temp = set()
    for i in os.listdir(path):
        i = i.split("_")[0]
        temp.add(i)
    temp = list(temp)
    print(len(temp))

    temp = ["S1BW000074016", "S1BW000074028", "S1BW000074086", "S1BW000093098", "S1BW000178007", "S1BW000178012",
            "S1BW000178013", "S1BW000178072", "S1NW001355015", "T1NF004789178", "T1BY000399096", "T1NF000935124",
            "S1BW000178152", "S1BW000181017", "S1BW000181036", "S1BW000181040", "S1BW000181047", "S1BW000181140",
            "S1BW000181142", "S1BW000334010", "S1BW000835059", "S1BW001490059", "S1NW004789044", "S1BW000130006",
            "S1NB000181183", "S1BW060289094", "S1BW004789112", "S1BW000300037", "S1BW000300159", "DBBK000196111",
            "DBBK000196115", "CFBA020018015", "S1NB014821290", "CFBA020018005", "T1NF000093111", "DFBK001171044",
            "T1BF000048173", "GFBV000227006", "S1BB000463008", "T1NF000048117", "S1NH006240112", "S1BW000178009",
            "GFBH000257023", "T1NF000093112", "S1NG000395035", "S1BB000300174", "T1NF014821156", "T1NF000093116",
            "SYN2000432072", "T1NY014821170", "GFBH070094019", "T1NF000935118", "T1NF004789155", "S1NW014821278",
            "GFBH070155017", "T1NF001522118", "S1BB000083045", "T1NY000074191", "DFNK002068016", "S1BG007249018",
            "T1NS000048142", "S1BB000181166", "GFNV000081013", "T1NF000935116", "S1NW000048041", "GFNV000227007",
            "T1NF000048133", "S1BW014821111", "T1NF014821231", "S1NB000071145", "S1BW000004083", "T1NF014821155",
            "T1BH000432242", "S1BW005922084", "S1NW000181081", "T1NS000106021", "S1NB000300265", "S1NW014821296",
            "S1BH001469028", "S1BW000048018", "SYN2014821072", "S1BW000029023", "T1NH000925018", "T1NS000837072",
            "T1NF004789165", "S1BW014894139", "T1NS000048125", "S1NW000300323", "S1BW000181027", "T1NF001522111",
            "S1BB000181157", "T1NF004789195", "S1BW000048031", "T1NS004789169", "S1NF000432193", "S1NB016112042",
            "T1NH000300361", "S1BW000048019", "T1NF000048149", "T1NY014821238"]

    dest1 = os.path.join(downloads, 'sbi_11th_temp1')

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
