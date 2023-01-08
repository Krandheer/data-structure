from collections import Counter


def get_keyword(keyword, look_for):
    # look for switch related keyword
    if look_for in ['C1', 'C2', 'C3', 'C4']:
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

    # look for counter related keys
    elif look_for in ['TYPE1', 'TYPE2', 'TYPE3', 'TYPE4', 'TYPE5']:
        if keyword in ['+CASSETTE', 'CASSETTE', 'SETTE', 'CASS', 'CST'] or "CASSETTE" in keyword:
            return 'CASSETTE'
        elif keyword in ['+REJECTED', 'REJECTED', '+REJ', 'REJ', 'PURG'] or "REJECTED" in keyword:
            return 'REJECTED'
        elif keyword in ['=REMAINING', "REAINING" 'REMAINING', '=REMAIN',
                         'REMAIN' '+REM' 'REM'] or 'REMAINING' in keyword:
            return 'REMAINING'
        elif keyword in ['+DISPENSED', 'DISPENSED', '+DISPEN', 'DISPEN' '+DISP', 'DISP', 'OISP',
                         '0ISP'] or "DISPENSED" in keyword:
            return 'DISPENSED'
        elif keyword in ['=TOTAL', 'TOTAL'] or "TOTAL" in keyword:
            return 'TOTAL'


def get_value_sticked_with_keyword(keyword_value):
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


def is_triangulation_pass(resp, look_for):
    # for switches
    # str+inc-dec-out=end
    if look_for in ['C1', 'C2', 'C3', 'C4']:  # means we are looking in counter
        return resp['STR']['value'] + resp['INC']['value'] - resp['DEC']['value'] - resp['OUT']['value'] == resp['END'][
            'value']

    # for counter
    elif look_for in ['TYPE1', 'TYPE2', 'TYPE3', 'TYPE4']:
        return resp['REMAINING']['value'] == resp['CASSETTE']['value'] + resp['REJECTED']['value'] and \
               resp['REMAINING']['value'] + resp['DISPENSED']['value'] == resp['TOTAL']['value']


def form_counter_resp(value, key_val, resp, look_for, temp):
    # if isnumeric is false then may be value has some alpha character in end or start which can be
    # cleaned using regex or other logic later, write function that checks if first character is digit, if yes then
    # take all digit starting from first till you get none digit character, else check end and if digit then go back
    # till you encounter none digit character
    for v in value:
        for index, row in enumerate(v):
            keyword = get_keyword(row['text'], look_for)
            if keyword in ['CASSETTE', 'REJECTED', 'REMAINING', 'DISPENSED', 'TOTAL']:
                value_co_ord = "NA"
                if row['text'][-5:].isnumeric():
                    denom_value = get_value_sticked_with_keyword(row['text'])
                    value_co_ord = row['pts']
                elif v[index + temp]['text'].isnumeric():
                    if len(v[index + temp]['text']) > 5:
                        if int(v[index + temp]['text'][:5]) == 0:
                            denom_value = 0
                        elif int(v[index + temp]["text"][-5:]) == 0:
                            denom_value = 0
                        else:
                            denom_value = int(v[index + temp]['text'][:5])
                        value_co_ord = v[index + temp]['pts']
                    else:
                        denom_value = int(v[index + temp]['text'])
                        value_co_ord = v[index + temp]['pts']
                else:
                    denom_value = get_value_sticked_with_keyword(v[index + temp]['text'])
                resp[keyword] = {'value': denom_value,
                                 'value_co_ord': value_co_ord,
                                 'key_co_ords': row['pts']}
            if index == len(v) - 2:
                resp['final_col_hdr_'] = look_for

    # add other field that were already present and need not be modified
    resp_keys = resp.keys()
    for key in key_val.keys():
        if key not in resp_keys:
            resp[key] = key_val[key]


def helper_row_based_extraction(look_for, key_val, ocr_resp):
    resp = {}
    ocr_resp_row = []
    switch_change_values = {}
    # switch_res_row will contain value for type1 and type2 under key type1 and for type3 and 4 under key type2
    counter_res_row = {}

    # for switches
    if look_for in ['C1', 'C2', 'C3', 'C4']:
        for res in ocr_resp:
            if res[0]['text'] == look_for:
                ocr_resp_row.append(res)
        for rows in ocr_resp_row:
            for index, row in enumerate(rows):
                # may be wrap in try block from here on
                keyword = get_keyword(row['text'], look_for)
                value = 0
                if keyword in ['STR', 'INC', 'DEC', 'OUT', 'END']:
                    if index + 1 < len(rows):
                        # value is related to bank and not keyword, distance function will do better job in that
                        # case, so take value of that
                        if 'XXX' in rows[index + 1]['text']:
                            value = key_val[keyword]['value']
                            value_co_ords = key_val[keyword]['value_co_ords']
                            key_co_ords = key_val[keyword]['key_co_ords']

                        elif rows[index + 1]['text'].isnumeric():
                            value = int(rows[index + 1]['text'])
                            value_co_ords = rows[index + 1]['pts']
                            key_co_ords = row['pts']

                        # check alpha_numeric and extract values from end or start
                        elif rows[index + 1]['text'].isalnum():
                            value = get_value_sticked_with_keyword(rows[index + 1]['text'])
                            value_co_ords = rows[index + 1]['pts']
                            key_co_ords = row['pts']

                        # handles space between values
                        elif len(rows[index + 1]['text'].split(" ")) >= 1:
                            temp_value = rows[index + 1]['text'].split(" ")
                            is_number = True
                            for temp in temp_value:
                                if not temp.isdigit():
                                    is_number = False
                                    break
                            if is_number:
                                value = int(''.join(rows[index + 1]['text'].split(" ")))
                            value_co_ords = rows[index + 1]['pts']
                            key_co_ords = row['pts']

                        else:
                            value = key_val[keyword]['value']
                            if "value_co_ords" in key_val[keyword].keys():
                                value_co_ords = key_val[keyword]['value_co_ords']
                            else:
                                value_co_ords = "NA"
                            if "key_co_ords" in key_val[keyword].keys():
                                key_co_ords = key_val[keyword]['key_co_ords']
                            else:
                                key_co_ords = "NA"

                        resp[keyword] = {'value': value,
                                         'value_co_ords': value_co_ords,
                                         'key_co_ords': key_co_ords}

                        for key_val_keywords in key_val.keys():
                            if keyword in key_val_keywords:
                                if value != key_val[key_val_keywords]["value"]:
                                    switch_change_values[keyword] = True
                if keyword == 'END':
                    resp['CTR'] = look_for

        # check if key-val that were present before in extraction is there or not, if not then add
        resp_keys = resp.keys()
        for key in key_val.keys():
            if key not in resp_keys:
                resp[key] = key_val[key]
    # for counter
    elif look_for in ['TYPE1', 'TYPE2', 'TYPE3', 'TYPE4', 'TYPE5']:
        temp = 0
        for res in ocr_resp:
            if res[0]['text'] == 'TYPE':
                temp = temp + 1
                counter_res_row[f'type{temp}'] = []
                continue
            if temp > 0:
                counter_res_row[f'type{temp}'].append(res)

        if look_for == 'TYPE1':
            value = counter_res_row['type1']
            form_counter_resp(value, key_val, resp, look_for, 1)

        elif look_for == 'TYPE2':
            value = counter_res_row['type1']
            form_counter_resp(value, key_val, resp, look_for, 2)

        elif look_for == 'TYPE3':
            value = counter_res_row['type2']
            form_counter_resp(value, key_val, resp, look_for, 1)

        elif look_for == 'TYPE4' or look_for == 'TYPE5':
            value = counter_res_row['type2']
            form_counter_resp(value, key_val, resp, look_for, 2)

    if is_triangulation_pass(resp, look_for):
        resp['TRIANGULATION'] = 'PASS'
        return resp

    # for switch: if only one value was changed and then also triangulation is failing try triangulation by making
    # that value 0, and do this on inc, dec, out as they have high chance of being 0.
    if len(switch_change_values) == 1:
        for key in switch_change_values.keys():
            if key in ['INC', "DEC", "OUT"]:
                resp[key]['value'] = 0
        if is_triangulation_pass(resp, look_for):
            resp['TRIANGULATION'] = "PASS"
            return resp

    # one extra or less value check for switch
    if not is_triangulation_pass(key_val, look_for):
        extra_digit_check = {}
        key_to_change_val = None
        for key, val in key_val.items():
            if key in ["STR", "INC", "DEC", "OUT", "OUT2", "END"]:
                extra_digit_check[key] = key_val[key]
        val_lengths = {key: len(str(val['value'])) for key, val in extra_digit_check.items() if val['value'] != 0}

        val_len_counts = Counter(val_lengths.values())

        # find the odd one that has greater or less value than most and eleminate one from left or right if more or add
        # one more of same value in left or right if less and check triangulation
        if len(val_len_counts) == 2:
            lowest_val_key = []
            min_occurence = min(val_len_counts.values())
            if min_occurence == 1:
                lowest_val_key = [key for key, value in val_len_counts.items() if value == min_occurence]
            if len(lowest_val_key) == 1:
                for key, val in val_lengths.items():
                    if val == lowest_val_key[0]:
                        key_to_change_val = key

        # handling only remove case, can be handled for add case as well which is not done yet
        remove_left, remove_right = 0, 0
        add_left, add_right = 0, 0
        if key_to_change_val:
            remove_left = int(str(extra_digit_check[key_to_change_val]['value'])[1:])
            remove_right = int(str(extra_digit_check[key_to_change_val]['value'])[:-1])
            add_left = int(str(extra_digit_check[key_to_change_val]['value'])[0:1] + str(
                extra_digit_check[key_to_change_val]['value']))
            add_right = int(
                str(extra_digit_check[key_to_change_val]['value']) + str(extra_digit_check[key_to_change_val]['value'])[
                                                                     -1:])

        if key_to_change_val in ['STR', "DEC", "INC", "OUT", "OUT2", "END"]:
            key_val[key_to_change_val]['value'] = remove_left
            if is_triangulation_pass(key_val, look_for):
                key_val['TRIANGULATION'] = 'PASS'
                return key_val
            key_val[key_to_change_val]['value'] = remove_right
            if is_triangulation_pass(key_val, look_for):
                key_val['TRIANGULATION'] = 'PASS'
                return key_val

            key_val[key_to_change_val]['value'] = add_left
            if is_triangulation_pass(key_val, look_for):
                key_val['TRIANGULATION'] = 'PASS'
                return key_val
            key_val[key_to_change_val]['value'] = add_right
            if is_triangulation_pass(key_val, look_for):
                key_val['TRIANGULATION'] = 'PASS'
                return key_val

    return None


def fraud_end_correction(look_for, key_val, ocr_resp):
    ocr_resp_row = []
    resp = {}

    if look_for in ['C1', 'C2', 'C3', 'C4']:
        for res in ocr_resp:
            if res[0]['text'] == look_for:
                ocr_resp_row.append(res)

    if key_val['END']["value_co_ords"] != "NA":
        return key_val
    for rows in ocr_resp_row:
        for index, row in enumerate(rows):
            keyword = get_keyword(row['text'], look_for)
            value = 0
            if keyword == 'END':
                if index + 1 < len(rows):
                    if rows[index + 1]['text'].isnumeric():
                        value = int(rows[index + 1]['text'])
                    else:
                        value = get_value_sticked_with_keyword(rows[index + 1]['text'])
                    resp[keyword] = {'value': value,
                                     'value_co_ords': rows[index + 1]['pts'],
                                     'key_co_ords': row['pts']}

    if "END" in key_val.keys() and "END" not in resp.keys():
        return key_val
    else:
        for key in key_val.keys():
            if key not in resp.keys() and key != "END":
                resp[key] = key_val[key]

    return resp


def helper_fields_extract(extracted_resp, slip_type, ocr_resp):
    for key in extracted_resp.keys():
        if slip_type == "SWITCH" and key in ['Counter#0', "Counter#1", "Counter#2", "Counter#3", 'Counter#4',
                                             'Counter#5', 'Counter#6']:
            print('randheer called')
            key_val = extracted_resp[key]
            if key_val['TRIANGULATION'] != 'PASS':
                print('randheer code used')
                look_for = key_val["CTR"]
                key_val_1 = {}
                for key1, val1 in key_val.items():
                    if key1 == "OUT2":
                        key_val_1['OUT'] = key_val["OUT2"]
                    else:
                        key_val_1[key1] = key_val[key1]
                helper_resp = helper_row_based_extraction(look_for, key_val_1, ocr_resp)

                if helper_resp is not None:
                    extracted_resp[key] = helper_resp
            if extracted_resp['FRAUD_END'] == 'YES' and key_val['TRIANGULATION'] == 'PASS':
                look_for = key_val["CTR"]
                helper_resp = fraud_end_correction(look_for, key_val, ocr_resp)
                if helper_resp is not None:
                    extracted_resp[key] = helper_resp

        elif slip_type == 'COUNTER' and key in ['TYPE1', 'TYPE2', 'TYPE3', 'TYPE4', 'TYPE5']:
            print('randheer called')
            key_val = extracted_resp[key]
            if key_val['TRIANGULATION'] != 'PASS':
                print("randheer code used")
                look_for = key_val['final_col_hdr_']
                helper_resp = helper_row_based_extraction(look_for, key_val, ocr_resp)

                if helper_resp is not None:
                    extracted_resp[key] = helper_resp

    if slip_type == "SWITCH":
        end_val_co_ord = "NA"
        for key, val in extracted_resp.items():
            if len(val) == 0:
                continue
            elif key in ['Counter#0', "Counter#1", "Counter#2", "Counter#3", 'Counter#4', 'Counter#5',
                         'Counter#6'] and isinstance(val, dict):
                end_val_co_ord = "NA"
                look_for = val["CTR"]
                for k, v in val.items():
                    if k == 'END':
                        end_val_co_ord = v['value_co_ords']
                if look_for == "C5" and extracted_resp['FRAUD_END'] == "YES":
                    end_val_co_ord = "AN"
                    extracted_resp['FRAUD_END'] = "NO"

        extracted_resp['FRAUD_END'] = 'YES' if end_val_co_ord == 'NA' else 'NO'

    return extracted_resp


# print(helper_fields_extract(extracted_resp, 'COUNTER', ocr_resp))

"""
for different format type switch:
temp = 0
if res[0]['text'] == look_for or temp < 2:
    first_keyword = get_keyword_value(res[1]['text'])
    if first_keyword == "STR":
        temp = 0
    resp_row.append(res)
    temp = temp+1
"""
