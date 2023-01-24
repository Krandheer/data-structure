import os
from glob import glob

import pandas as pd
import json
import shutil

base_dir = os.path.expanduser('~')

downloads = os.path.join(base_dir, 'Downloads')

path_hdfc = os.path.join(downloads, 'hdfc.csv')
destination = os.path.join(downloads, 'hdfc')
df = pd.read_csv(path_hdfc)
atm_ids = []
for item in df['ATMID']:
    atm_ids.append(item)


def create_json():
    with open(f'{downloads}/hdfc.json', 'w') as f:
        json.dump({'hdfc': atm_ids}, f)


def move(src, desti):
    files_to_move = glob(f'{src}/{id}*')
    for temp in files_to_move:
        shutil.copy(temp, desti)


# here folder to move is destination
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
