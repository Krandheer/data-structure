import json
import os.path
from glob import glob

with open("rules/master_denom", "r") as fp:
    master_ll = fp.readlines()

# mapping of denom type based on atm_id
master_d = dict()
for elem in master_ll:
    arr = elem.strip("\n").split("$")
    if arr[0] in master_d:
        loc_d = master_d[arr[0]]
    else:
        loc_d = {}
    if 'S1AC' in arr[0] and arr[1].upper() not in loc_d:
        loc_d[arr[1].upper()] = int(arr[2])
    elif 'S1AC' not in arr[0]:
        loc_d[arr[1].upper()] = int(arr[2])
    master_d[arr[0]] = loc_d


def fix_counter(counter_type, switch_type, curr_files, atm_id, json_log_path):
    for file in curr_files:
        if switch_type in file:
            with open(file, "r") as f:
                switch_data = json.load(f)
        elif counter_type in file:
            with open(file, "r") as f:
                counter_data = json.load(f)
    is_modified = False
    for key, val in counter_data.items():
        # End, OUT and remaining, dispensed  can always be corrected in before
        # End, STR and remaining, total can always be corrected in after
        value_changed = False
        if key in ["TYPE1", "TYPE2", "TYPE3", "TYPE4", "TYPE5"] and val['TRIANGULATION'] == "FAIL":
            col_hdr = val['final_col_hdr_']
            ctr = f'C{col_hdr[-1]}'
            if f"T{col_hdr[-1]}" not in master_d[atm_id]:
                val['CASSETTE']['value'] = 0
                val['REJECTED']['value'] = 0
                val['REMAINING']['value'] = 0
                val['DISPENSED']['value'] = 0
                val['TOTAL']['value'] = 0
                is_modified = True
                value_changed = True

            elif f"T{col_hdr[-1]}" in master_d[atm_id]:
                denom = master_d[atm_id][f"T{col_hdr[-1]}"]  # need to define it
                temp = {}
                for s_key, s_val in switch_data.items():
                    if s_val["CTR"] == ctr:
                        temp = s_val
                        break
                if counter_type == "_CA":
                    if (val['TOTAL']['value']) * denom != temp['STR']['value'] and temp['INC']['value'] == 0:
                        val['TOTAL']['value'] = temp['STR']['value'] // denom
                        is_modified = True
                        value_changed = True
                    elif (val['TOTAL']['value']) * denom != (temp['STR']['value'] + temp['INC']['value']):
                        temp['TOTAL']['value'] = (temp['STR']['value'] + temp['INC']['value']) // denom
                        is_modified = True
                        value_changed = True
                    if (val['REMAINING']['value']) * denom != temp['END']['value']:
                        val['REMAINING']['value'] = temp['END']['value'] // denom
                        if val['REJECTED']['value'] == 0 and val['CASSETTE']['value'] != val['REMAINING']['value']:
                            val['CASSETTE']['value'] = val['REMAINING']['value']
                        is_modified = True
                        value_changed = True

                    if (val['REMAINING']['value']) * denom == temp['END']['value'] and val['REJECTED']['value'] == 0 \
                            and val['CASSETTE']['value'] != val['REMAINING']['value']:
                        val['CASSETTE']['value'] = val['REMAINING']['value']
                        is_modified = True
                        value_changed = True

                elif counter_type == "_CB":
                    if (val['DISPENSED']['value']) * denom != temp['OUT']['value']:
                        val['DISPENSED']['value'] = temp['OUT']['value'] // denom
                        is_modified = True
                        value_changed = True

                    if (val['REMAINING']['value']) * denom != temp['END']['value']:
                        val['REMAINING']['value'] = temp['END']['value'] // denom
                        if val['REJECTED']['value'] == 0 and val['CASSETTE']['value'] != val['REMAINING']['value']:
                            val['CASSETTE']['value'] = val['REMAINING']['value']
                        is_modified = True
                        value_changed = True

                    if (val['REMAINING']['value']) * denom == temp['END']['value'] and val['REJECTED']['value'] == 0 \
                            and val['CASSETTE']['value'] != val['REMAINING']['value']:
                        val['CASSETTE']['value'] = val['REMAINING']['value']
                        is_modified = True
                        value_changed = True

        if value_changed:
            try:
                if val['REMAINING']['value'] == val['CASSETTE']['value'] + val['REJECTED']['value'] and \
                        val['REMAINING']['value'] + val['DISPENSED']['value'] == val['TOTAL']['value']:
                    val['TRIANGULATION'] = "PASS"
                    with open(json_log_path, 'r') as f:
                        data = json.load(f)
                    data['pair_matching_patch'] += 1
                    data[atm_id] = 'pair_matching_patch'
                    with open(json_log_path, 'w') as f:
                        json.dump(data, f)
            except:
                pass
            counter_data[key] = val

    if is_modified:
        path = ""
        for file in curr_files:
            if counter_type in file:
                path = file
                break
        with open(path, "w") as f:
            json.dump(counter_data, f)


def fix_switch(switch_type, counter_type, curr_files, atm_id, json_log_path):
    for file in curr_files:
        if switch_type in file:
            with open(file, "r") as f:
                switch_data = json.load(f)
        elif counter_type in file:
            with open(file, "r") as f:
                counter_data = json.load(f)
    is_modified = False
    for key, val in switch_data.items():
        value_changed = False
        if key in ["Counter#0", "Counter#1", "Counter#2", "Counter#3", "Counter#4"] and \
                val['TRIANGULATION'] == "FAIL":
            ctr = val['CTR']
            if ctr not in master_d[atm_id]:
                val['STR']['value'] = 0
                val['INC']['value'] = 0
                val['DEC']['value'] = 0
                val['OUT']['value'] = 0
                val['END']['value'] = 0
            elif ctr in master_d[atm_id]:
                denom = master_d[atm_id][ctr]
                temp = {}
                if ctr in ['C1', 'C2', 'C3', 'C4']:
                    temp = counter_data[f"TYPE{ctr[-1]}"]
                elif ctr[-1] > 4:
                    temp = counter_data['TYPE4']
                # End, OUT and remaining, dispensed  can always be corrected in before
                # End, STR and remaining, total can always be corrected in after
                if switch_type == "_SA":
                    if val['STR']['value'] != (temp['TOTAL']['value']) * denom and val['INC']['value'] == 0:
                        val['STR']['value'] = (temp['TOTAL']['value']) * denom
                        is_modified = True
                        value_changed = True
                    elif val['STR']['value'] != (temp['TOTAL']['value']) * denom:
                        val['STR']['value'] = (temp['TOTAL']['value']) * denom - val['INC']['value']
                        is_modified = True
                        value_changed = True

                    if val['END']['value'] != (temp['REMAINING']['value']) * denom:
                        val['END']['value'] = (temp['REMAINING']['value']) * denom
                        is_modified = True
                        value_changed = True

                elif switch_type == "_SB":
                    if val['OUT']['value'] != (temp['DISPENSED']['value']) * denom or val['END']['value'] != (
                            temp['REMAINING']['value']) * denom:
                        val['OUT']['value'] = (temp['DISPENSED']['value']) * denom
                        val['END']['value'] = (temp['REMAINING']['value']) * denom
                        is_modified = True
                        value_changed = True
        if value_changed:
            try:
                if val['STR']['value'] + val['INC']['value'] - val['DEC']['value'] - val['OUT']['value'] == val['END'][
                    'value']:
                    val['TRIANGULATION'] = "PASS"
                    switch_data['FRAUD_END'] = "NO"  #newline added 27feb
                    with open(json_log_path, 'r') as f:
                        data = json.load(f)
                    data['pair_matching_patch'] += 1
                    data[f"pair_{atm_id}"] = 'pair_matching_patch'
                    with open(json_log_path, 'w') as f:
                        json.dump(data, f)


            except:
                pass
            switch_data[key] = val
    if is_modified:
        path = ""
        for file in curr_files:
            if switch_type in file:
                path = file
                break
        with open(path, "w") as f:
            json.dump(switch_data, f)


def process_pass_fail(data, pass_fail, slip_type):
    if slip_type in ["CA", "CB"]:
        for key, val in data.items():
            if key in ["TYPE1", "TYPE2", "TYPE3", "TYPE4", "TYPE5"]:
                if val["TRIANGULATION"] == "FAIL":
                    pass_fail[slip_type] = 'fail'
    elif slip_type in ["SA", "SB"]:
        for key, val in data.items():
            if key in ["Counter#0", "Counter#1", "Counter#2", "Counter#3", "Counter#4"]:
                if val["TRIANGULATION"] == "FAIL":
                    pass_fail['SA'] = 'fail'


def switch_counter_sync(atm_id, INTERMEDIATE_JSON_PATH, json_log_path):
    print(f'entering in patch2->{atm_id}')
    curr_files = glob(f"{INTERMEDIATE_JSON_PATH}/{atm_id}*")
    pass_fail = {}

    for file in curr_files:
        with open(file, 'r') as f:
            data = json.load(f)
            if "_CA" in file:
                process_pass_fail(data, pass_fail, "CA")
            if "_CB" in file:
                process_pass_fail(data, pass_fail, "CB")

            if "_SA" in file:
                process_pass_fail(data, pass_fail, "SA")
            if "_SB" in file:
                process_pass_fail(data, pass_fail, "SB")
    if not pass_fail:
        return
    if "SA" in pass_fail and not "CA" in pass_fail:
        fix_switch("_SA", "_CA", curr_files, atm_id, json_log_path)

    if "SB" in pass_fail and not "CB" in pass_fail:
        fix_switch("_SB", "_CB", curr_files, atm_id, json_log_path)

    if 'CA' in pass_fail and not "SA" in pass_fail:
        fix_counter("_CA", "_SA", curr_files, atm_id, json_log_path)

    if "CB" in pass_fail and not "SB" in pass_fail:
        fix_counter("_CB", "_SB", curr_files, atm_id, json_log_path)


home = os.path.expanduser("~")
path = os.path.join(home, 'projects', 'WriterCorp', 'INTERMEDIATE_JSON_PATH')
json_log_path = 'resp.json'
switch_counter_sync('S1ANBH16', path, json_log_path)
