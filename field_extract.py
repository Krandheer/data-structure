import copy
import json
import os.path


def get_keyword(keyword, look_for):
    if look_for == "is_counter":
        if keyword in ['+CASSETTE', 'CASSETTE', 'SETTE', 'CASS', 'CST'] or "CASSETTE" in keyword:
            return 'CASSETTE'
        elif keyword in ['+REJECTED', 'REJECTED', '+REJ', 'REJ', 'PURG'] or "REJECTED" in keyword:
            return 'REJECTED'
        elif keyword in ['=REMAINING', "REAINING" 'REMAINING', '=REMAIN',
                         'REMAIN' '+REM' 'REM'] or 'REMAINING' in keyword:
            return 'REMAINING'
        elif keyword in ['+DISPENSED', 'DISPENSED', '+DISPEN', 'DISPEN' '+DISP', 'DISP', 'OISP',
                         '0ISP', "DISPENS"] or "DISPENSED" in keyword:
            return 'DISPENSED'
        elif keyword in ['=TOTAL', 'TOTAL'] or "TOTAL" in keyword:
            return 'TOTAL'

    elif look_for == "is_switch":
        if keyword in ['STR', 'ST']:
            return 'STR'
        elif keyword in ['INC', 'IC']:
            return 'INC'
        elif keyword in ['OUT', "OU", "OC"]:
            return 'OUT'
        elif keyword in ['DEC', 'DC']:
            return 'DEC'
        elif keyword in ['END', 'EC']:
            return 'END'


def get_sticked_value(keyword_value):
    value = ''
    if keyword_value[-1].isnumeric():
        i = len(keyword_value) - 1
        while i > -1 and keyword_value[i].isnumeric():
            value += keyword_value[i]
            i -= 1
        return int(value[::-1])
    elif keyword_value[0].isnumeric():
        i = 0
        while keyword_value[i].isnumeric():
            value += keyword_value[i]
            i += 1
        return int(value)
    return 0


def counter_val(counter1_val, ocr_resp, look_for):
    counter_values = ocr_resp[look_for]
    for index, c in enumerate(counter_values):
        if not c:
            counter_values.pop(index)
    counter_values = sorted(counter_values, key=lambda x: x[0]['pts'][0][1])
    keyword_seen = {}
    for rows in counter_values:
        after_keyword = False
        current_keyword = ''

        # if numerical values with keyword then extract that and add in response
        for row in rows:
            keyword = get_keyword(row['text'], "is_counter")
            if keyword in ['CASSETTE', 'REJECTED', 'REMAINING', 'DISPENSED', 'TOTAL']:
                current_keyword = keyword
                after_keyword = True
                if not keyword in keyword_seen.keys():
                    keyword_seen[keyword] = 1
                    counter1_val['type_1_2'][current_keyword] = []
                    # if numerical values with keyword then extract that and add it in response here itself
                    continue
                else:
                    keyword_seen[keyword] = keyword_seen[keyword] + 1
                    counter1_val['type_3_4'][current_keyword] = []
                    continue
            if after_keyword and current_keyword:
                if keyword_seen[current_keyword] == 1:
                    counter1_val['type_1_2'][current_keyword].append(row)
                elif keyword_seen[current_keyword] == 2:
                    counter1_val['type_3_4'][current_keyword].append(row)
    return counter1_val


def is_triangulation_pass(resp, look_for):
    # for switches
    # str+inc-dec-out=end
    if look_for in ['Counter#0', 'Counter#1', 'Counter#2', 'Counter#3']:  # means we are looking in counter
        return resp['STR']['value'] + resp['INC']['value'] - resp['DEC']['value'] - resp['OUT']['value'] == resp['END'][
            'value']

    # for counter
    elif look_for in ['TYPE1', 'TYPE2', 'TYPE3', 'TYPE4']:
        return resp['REMAINING']['value'] == resp['CASSETTE']['value'] + resp['REJECTED']['value'] and \
               resp['REMAINING']['value'] + resp['DISPENSED']['value'] == resp['TOTAL']['value']


def form_counter_resp(counter_value, counter_resp):
    for key, val in counter_value.items():
        if key == 'type_1_2':
            type1 = {}
            type2 = {}
            for k, v in val.items():
                if k in ['CASSETTE', 'REJECTED', 'REMAINING', 'DISPENSED', 'TOTAL']:
                    value1, value2 = 0, 0
                    value_co_ord1, value_co_ord2 = [], []
                    type_1_val = False
                    for index, denom_value in enumerate(v):
                        if not type_1_val:
                            temp = denom_value['text']
                            if temp.isnumeric() and len(temp) >= 3:
                                value1 = int(temp)
                                type_1_val = True

                            elif temp.isalnum() and len(temp) > 3:
                                value1 = get_sticked_value(temp)
                                type_1_val = True

                            elif len(temp) < 3 and len(v) > index + 2:
                                continue
                            value_co_ord1 = denom_value['pts']
                        elif type_1_val:
                            temp = denom_value['text']
                            if temp.isnumeric() and len(temp) >= 3:
                                value2 = int(temp)
                                break

                            elif temp.isalnum() and len(temp) > 3:
                                value2 = get_sticked_value(temp)
                                break

                            elif len(temp) < 3 and len(v) >= index + 2:
                                continue
                            value_co_ord2 = denom_value['pts']

                    type1[k] = {'value': value1, "value_co_ord": value_co_ord1}
                    type2[k] = {'value': value2, "value_co_ord": value_co_ord2}
            counter_resp['TYPE1'] = type1
            counter_resp["TYPE2"] = type2
        elif key == 'type_3_4':
            type3 = {}
            type4 = {}
            for k, v in val.items():
                if k in ['CASSETTE', 'REJECTED', 'REMAINING', 'DISPENSED', 'TOTAL']:
                    value3, value4 = 0, 0
                    value_co_ord3, value_co_ord4 = [], []
                    type_3_val = False
                    for index, denom_value in enumerate(v):
                        if not type_3_val:
                            temp = denom_value['text']
                            if temp.isnumeric() and len(temp) >= 3:
                                value3 = int(temp)
                                type_3_val = True

                            elif temp.isalnum():
                                value3 = get_sticked_value(temp)
                                type_3_val = True

                            elif len(temp) < 3 and len(v) > index + 2:
                                continue
                            value_co_ord3 = denom_value['pts']
                        elif type_3_val:
                            temp = denom_value['text']
                            if temp.isnumeric() and len(temp) >= 3:
                                value4 = int(temp)
                                break

                            elif temp.isalnum():
                                value4 = get_sticked_value(temp)
                                break

                            elif len(temp) < 3 and len(v) >= index + 2:
                                continue
                            value_co_ord4 = denom_value['pts']

                    type3[k] = {'value': value3, "value_co_ord": value_co_ord3}
                    type4[k] = {'value': value4, "value_co_ord": value_co_ord4}
            counter_resp['TYPE3'] = type3
            counter_resp["TYPE4"] = type4

    # do triangulation
    resp = copy.deepcopy(counter_resp)
    for key, value in resp.items():
        if key in ['TYPE1', 'TYPE2', 'TYPE3', 'TYPE4']:
            try:
                if is_triangulation_pass(value, key):
                    counter_resp[key]['final_col_hdr_'] = key
                    counter_resp[key]['TRIANGULATION'] = "PASS"
                else:
                    counter_resp[key]['final_col_hdr_'] = key
                    counter_resp[key]['TRIANGULATION'] = "FAIL"

            except:
                counter_resp[key]['final_col_hdr_'] = key
                counter_resp[key]['TRIANGULATION'] = "FAIL"


def form_switch_resp(switch_val, index, switch_resp, look_for):
    if index + 2 < len(switch_val):
        keyword = get_keyword(switch_val[index + 1]['text'], 'is_switch')
        value = 0
        key_co_ords = []
        value_co_ords = []
        if keyword in ['STR', 'INC', 'DEC', 'OUT', 'END']:
            counter = {}
            if switch_val[index + 2]['text'].isnumeric():
                value = int(switch_val[index + 2]['text'])
                value_co_ords = switch_val[index + 2]['pts']
                key_co_ords = switch_val[index + 1]['pts']

            # handles value that has some alpha character from background
            elif switch_val[index + 2]['text'].isalnum():
                value = get_sticked_value(switch_val[index + 2]['text'])
                value_co_ords = switch_val[index + 2]['pts']
                key_co_ords = switch_val[index + 1]['pts']

            # handles space between
            elif len(switch_val[index + 2]['text'].split(" ")) >= 1:
                temp_value = switch_val[index + 2]['text'].split(" ")
                is_number = True
                for temp in temp_value:
                    if not temp.isdigit():
                        is_number = False
                        break
                if is_number:
                    value = int(''.join(switch_val[index + 2]['text'].split(" ")))
                value_co_ords = switch_val[index + 2]['pts']
                key_co_ords = switch_val[index + 1]['pts']
            if look_for == "C1":
                switch_resp['Counter#0'][keyword] = {"value": value, 'value_co_ord': value_co_ords,
                                                     'key_co_ords': key_co_ords}
            elif look_for == "C2":
                switch_resp['Counter#1'][keyword] = {"value": value, 'value_co_ord': value_co_ords,
                                                     'key_co_ords': key_co_ords}
            elif look_for == "C3":
                switch_resp['Counter#2'][keyword] = {"value": value, 'value_co_ord': value_co_ords,
                                                     'key_co_ords': key_co_ords}
            elif look_for in ['C4', "C5"]:
                switch_resp['Counter#3'][keyword] = {"value": value, 'value_co_ord': value_co_ords,
                                                     'key_co_ords': key_co_ords}


def switch_val(switch_val, ocr_resp, look_for, switch_resp):
    switch_values = ocr_resp[look_for]
    for values in switch_values:
        to_append = False
        for val in values:
            if val['text'] in ["C1", "C2", "C3", "C4"]:
                switch_val.append(val)
                to_append = True
                continue
            if to_append:
                switch_val.append(val)
    # form switch response
    for index, row in enumerate(switch_val):
        if row['text'] == 'C1':
            form_switch_resp(switch_val, index, switch_resp, "C1")
        elif row['text'] == 'C2':
            form_switch_resp(switch_val, index, switch_resp, "C2")
        elif row['text'] == "C3":
            form_switch_resp(switch_val, index, switch_resp, "C3")

        elif row['text'] in ['C4', 'C5']:
            form_switch_resp(switch_val, index, switch_resp, row['text'])

    resp = copy.deepcopy(switch_resp)
    for key, value in resp.items():
        if key in ['Counter#0', 'Counter#1', 'Counter#2', 'Counter#3']:
            try:
                if is_triangulation_pass(value, key):
                    switch_resp[key]['CTR'] = int(key[-1]) + 1
                    switch_resp[key]['TRIANGULATION'] = "PASS"
                else:
                    switch_resp[key]['CTR'] = int(key[-1]) + 1
                    switch_resp[key]['TRIANGULATION'] = "FAIL"
            except:
                switch_resp[key]['CTR'] = int(key[-1]) + 1
                switch_resp[key]['TRIANGULATION'] = "FAIL"

    return switch_resp


def extract_fields(ocr_resp):
    counter1_val = {'type_1_2': {}, "type_3_4": {}}
    counter2_val = {'type_1_2': {}, "type_3_4": {}}
    counter1_resp = {}
    counter2_resp = {}
    switch1_val = []
    switch2_val = []
    switch1_resp = {'Counter#0': {}, 'Counter#1': {}, 'Counter#2': {}, 'Counter#3': {}}
    switch2_resp = {'Counter#0': {}, 'Counter#1': {}, 'Counter#2': {}, 'Counter#3': {}}

    counter1_val = counter_val(counter1_val, ocr_resp, 'Counter1')
    counter2_val = counter_val(counter2_val, ocr_resp, 'Counter2')

    switch1_resp = switch_val(switch1_val, ocr_resp, 'Switch1', switch1_resp)
    switch2_resp = switch_val(switch2_val, ocr_resp, 'Switch2', switch2_resp)

    # form counter one response
    form_counter_resp(counter1_val, counter1_resp)
    form_counter_resp(counter2_val, counter2_resp)
    result = {'counter1': counter1_resp, 'counter2': counter2_resp, 'switch1': switch1_resp, 'switch2': switch2_resp}
    return result

#
# print(extract_fields(ocr_resp))
