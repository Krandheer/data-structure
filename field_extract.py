import copy


def get_keyword(keyword, is_counter):
    if is_counter:
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
            keyword = get_keyword(row['text'], True)
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
    if look_for in ['C1', 'C2', 'C3', 'C4']:  # means we are looking in counter
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
                    for index, denom_value in enumerate(v):
                        if index == 0:
                            temp = denom_value['text']
                            if temp.isnumeric():
                                value1 = int(temp)
                            else:
                                value1 = get_sticked_value(temp)
                            value_co_ord1 = denom_value['pts']
                        elif index == 1:
                            temp = denom_value['text']
                            if temp.isnumeric():
                                value2 = int(temp)
                            else:
                                value2 = get_sticked_value(temp)
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
                    for index, denom_value in enumerate(v):
                        if index == 0:
                            temp = denom_value['text']
                            if temp.isnumeric():
                                value3 = int(temp)
                            else:
                                value3 = get_sticked_value(temp)
                            value_co_ord3 = denom_value['pts']
                        elif index == 1:
                            temp = denom_value['text']
                            if temp.isnumeric():
                                value4 = int(temp)
                            else:
                                value4 = get_sticked_value(temp)
                            value_co_ord4 = denom_value['pts']

                    type3[k] = {'value': value3, "value_co_ord": value_co_ord3}
                    type4[k] = {'value': value4, "value_co_ord": value_co_ord4}
            counter_resp['TYPE3'] = type3
            counter_resp["TYPE4"] = type4

    # do triangulation
    resp = copy.deepcopy(counter_resp)
    for key, value in resp.items():
        if key in ['TYPE1', 'TYPE2', 'TYPE3', 'TYPE4']:
            if is_triangulation_pass(value, key):
                counter_resp[key]['final_col_hdr_'] = key
                counter_resp[key]['TRIANGULATION'] = "PASS"
            else:
                counter_resp[key]['final_col_hdr_'] = key
                counter_resp[key]['TRIANGULATION'] = "FAIL"


def extract_fields(ocr_resp):
    counter1_val = {'type_1_2': {}, "type_3_4": {}}
    counter2_val = {'type_1_2': {}, "type_3_4": {}}
    counter1_resp = {}
    counter2_resp = {}

    counter1_val = counter_val(counter1_val, ocr_resp, 'Counter1')
    counter2_val = counter_val(counter2_val, ocr_resp, 'Counter2')

    # form counter one response
    form_counter_resp(counter1_val, counter1_resp)
    form_counter_resp(counter2_val, counter2_resp)

    return counter2_resp,

#
# print(extract_fields(ocr_resp))
