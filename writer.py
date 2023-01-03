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
    elif look_for in ['type1', 'type2', 'type3', 'type4']:
        if keyword in ['+CASSETTE', 'CASSETTE', 'SETTE', 'CASS', 'CST']:
            return 'CASSETTE'
        elif keyword in ['+REJECTED', 'REJECTED', '+REJ', 'REJ', 'PURG']:
            return 'REJECTED'
        elif keyword in ['=REMAINING', 'REMAINING', '=REMAIN', 'REMAIN' '+REM' 'REM']:
            return 'REMAINING'
        elif keyword in ['+DISPENSED', 'DISPENSED', '+DISPEN', 'DISPEN' '+DISP', 'DISP', 'OISP', '0ISP']:
            return 'DISPENSED'
        elif keyword in ['=TOTAL', 'TOTAL']:
            return 'TOTAL'


def get_keyword_value(keyword_value):
    value = ''
    if keyword_value[0].isnumeric():
        i = 0
        while keyword_value[i].isnumeric():
            value += keyword_value[i]
            i += 1
        return int(value)
    elif keyword_value[-1].isnumeric():
        i = len(keyword_value) - 1
        while i > -1 and keyword_value[i].isnumeric():
            value += keyword_value[i]
            i -= 1
        return int(value)
    return 0


def is_triangulation_pass(resp, look_for):
    # for switches
    # str+inc-dec-out=end
    if look_for in ['C1', 'C2', 'C3', 'C4']:  # means we are looking in counter
        return resp['STR']['value'] + resp['INC']['value'] - resp['DEC']['value'] - resp['OUT']['value'] == resp['END'][
            'value']

    # for counter
    elif look_for in ['type1', 'type2', 'type3', 'type4']:
        return resp['REMAINING']['value'] == resp['CASSETTE']['value'] + resp['REJECTED']['value'] and \
               resp['REMAINING']['value'] + resp['DISPENSED']['value'] == resp['TOTAL']['value']


def form_counter_resp(value, resp, look_for, temp):
    # if isnumeric is false then may be value has some alpha character in end or start which can be
    # cleaned using regex or other logic later, write function that checks if first character is digit, if yes then
    # take all digit starting from first till you get none digit character, else check end and if digit then go back
    # till you encounter none digit character
    for v in value:
        for index, row in enumerate(v):
            keyword = get_keyword(row['text'], look_for)
            if keyword in ['CASSETTE', 'REJECTED', 'REMAINING', 'DISPENSED', 'TOTAL']:
                if v[index + temp]['text'].isnumeric():
                    denom_value = int(v[index + temp]['text'])
                else:
                    denom_value = get_keyword_value(v[index + temp]['text'])
                resp[keyword] = {'value': denom_value,
                                 'value_co_ord': v[index + temp]['pts'],
                                 'key_co_ords': row['pts']}
            if index == len(v) - 2:
                resp['final_col_hdr_'] = look_for


def helper_row_based_extraction(look_for, key_val, ocr_resp):
    resp = {}
    ocr_resp_row = []
    # switch_res_row will contain value for type1 and type2 under key type1 and for type3 and 4 under key type2
    counter_res_row = {}

    # for switches
    if look_for in ['C1', 'C2', 'C3', 'C4']:
        for res in ocr_resp:
            if res[0]['text'] == look_for:
                ocr_resp_row.append(res)
        for rows in ocr_resp_row:
            for index, row in enumerate(rows):
                keyword = get_keyword(row['text'], look_for)
                value = 0
                if keyword in ['STR', 'INC', 'DEC', 'OUT', 'END']:
                    if index + 1 < len(rows):
                        # value is related to bank and not keyword, distance function will do better job in that
                        # case, so take value of that
                        if 'XXX' in rows[index + 1]['text']:
                            value = key_val[keyword]['value']

                        elif rows[index + 1]['text'].isnumeric():
                            value = int(rows[index + 1]['text'])
                        else:
                            value = get_keyword_value(rows[index + 1]['text'])
                        resp[keyword] = {'value': value,
                                         'value_co_ords': rows[index + 1]['pts'],
                                         'key_co_ords': row['pts']}
                    # else:
                    #     resp[keyword] = {"value": key_val[keyword][value],
                    #                      'value_co_ords': key_val[keyword]["value_co_ords"],
                    #                      'key_co_ords': key_val[keyword]["key_co_ords"]}
                if keyword == 'END':
                    resp['CTR'] = look_for

        # check if key-val that were present before in extraction is there or not, if not then add
        key_val_keys = key_val.keys()
        resp_keys = resp.keys()
        for key in key_val_keys:
            if key not in resp_keys:
                resp[key] = key_val[key]
    # for counter
    elif look_for in ['type1', 'type2', 'type3', 'type4', 'type5']:
        temp = 0
        for res in ocr_resp:
            if res[0]['text'] == 'TYPE':
                temp = temp + 1
                counter_res_row[f'type{temp}'] = []
                continue
            if temp > 0:
                counter_res_row[f'type{temp}'].append(res)

        if look_for == 'type1':
            value = counter_res_row['type1']
            form_counter_resp(value, resp, look_for, 1)

        elif look_for == 'type2':
            value = counter_res_row['type1']
            form_counter_resp(value, resp, look_for, 2)

        elif look_for == 'type3':
            value = counter_res_row['type2']
            form_counter_resp(value, resp, look_for, 1)

        elif look_for == 'type4' or look_for == 'type5':
            value = counter_res_row['type2']
            form_counter_resp(value, resp, look_for, 2)

    if is_triangulation_pass(resp, look_for):
        resp['TRIANGULATION'] = 'PASS'
        return resp
    return None


def helper_fields_extract(extracted_resp, slip_type, ocr_resp):
    for key in extracted_resp.keys():
        if slip_type == "SWITCH" and key in ['Counter#0', "Counter#1", "Counter#2", "Counter#3", 'Counter#4',
                                             'Counter#5', 'Counter#6']:
            print('randheer called')
            key_val = extracted_resp[key]
            if key_val['TRIANGULATION'] != 'PASS':
                print('randheer code used')
                look_for = key_val["CTR"]
                helper_resp = helper_row_based_extraction(look_for, key_val, ocr_resp)

                if helper_resp is not None:
                    extracted_resp[key] = helper_resp

        elif slip_type == 'COUNTER' and key in ['TYPE1', 'TYPE2', 'TYPE3', 'TYPE4', 'TYPE5']:
            print('randheer called')
            key_val = extracted_resp[key]
            if key_val['TRIANGULATION'] != 'PASS':
                look_for = f'type{key[-1]}'
                helper_resp = helper_row_based_extraction(look_for, ocr_resp)

                if helper_resp is not None:
                    extracted_resp[key] = helper_resp

    if slip_type == "SWITCH":
        end_val_co_ord = None
        for key, val in extracted_resp.items():
            if len(val) == 0:
                continue
            if type(val) == "dict":
                for k, v in val.items():
                    if k == 'END':
                        end_val_co_ord = v['value_co_ords']
        extracted_resp['FRAUD_END'] = 'YES' if end_val_co_ord == 'NA' else 'NO'

    return extracted_resp


# print(helper_fields_extract(extracted_resp, 'SWITCH', ocr_resp))
