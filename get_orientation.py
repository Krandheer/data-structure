from utils.text_detection import TextDetection
import cv2
from main.DataLoader import DataLoader
from utils.deskew_method import deskew

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
import regex
import gc
import logging
import time
import imutils
import re

logging.basicConfig(filename='writer_ai.log', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

IMG_SIZE = (512, 64)


class FilePaths:
    ocr_model_dir = "ocr_saved_model/model_writer_prod_2"
    # ocr_model_file = os.path.join(ocr_model_dir,"epoch_57.h5")
    ocr_model_file = ocr_model_dir
    "filenames and paths to data"
    fnCharList = ocr_model_dir + '/charList.txt'
    fnAccuracy = ocr_model_dir + '/accuracy.txt'


host_address = "ec2-52-7-45-213.compute-1.amazonaws.com"
img_port = 8114

ocr_model = tf.keras.models.load_model(FilePaths.ocr_model_file, custom_objects={'keras': keras, 'tf': tf})

irr_rel_model_name = 'VGG_MODELS/REL_IRR_CLASS_3'
classify_model = load_model(irr_rel_model_name)

s3_bucket_name = 'vision-era-uploads'
bucket_location = ''
charlist = list(open(FilePaths.fnCharList).read())

other_kws = ['BANK', 'LAST', 'COUNT', 'CLEARED', 'DATE', 'TIME', 'TYPE']
counter_kws = ['SETTE', ' REJ', 'PURG', 'REMAIN', 'DISPEN', 'TYPE', 'DENO', 'CST', 'REM', 'DISP', 'ining', 'ensed',
               'urge', 'INR 0100', 'INR 0500', 'INR 0200', 'INR 02K']
not_counter_kws_1 = ['LOADED', 'BALANCE', 'SLOT']

switch_kws = [' C1', ' C2', ' C3', ' C4', ' C5']
switch_kws_4 = [' IC', ' OU', ' OC', ' DC', ' EC', ' ST']
switch_kws_2 = [' INC', ' DEC', ' END', ' STR', 'INC ', 'DEC ', 'STR ', 'END ', ' BEG', ' DSP', ' ADJ', 'BEG ', 'DSP ',
                'ADJ ']
switch_kws_3 = [' C1 ', ' C2 ', ' C3 ', ' C4 ', ' C5 ']
switch_kws_5 = [' IC ', ' OU ', ' OC ', ' DC ', ' EC ', ' ST ']


def contains_valid_switch_value(full_text):
    return len(re.findall(r'(\d{1,})(000)', full_text)) > 0


def decide_slip_type(body):
    # at least 2 kws for switch and 3 for counter
    sw_ctr, ctr_ctr, sw_ctr2, sw_ctr3, sw_ctr_probables_2, sw_ctr_probables_1, non_ctr_ctr_1, non_ctr_ctr_2 = set(), set(), set(), set(), set(), set(), set(), set()
    non_ctr_ctr_1 = []
    for orig_row in body.split("\n"):
        orig_row = " " + orig_row + " "
        if len(re.findall(r'(INR )(\d{4})', orig_row)) > 0:
            return 'COUNTER', 1
        row_sw_ctr, row_sw_ctr2, row_sw_ctr3, row_sw_ctr4, row_sw_ctr5 = set(), set(), set(), set(), set()
        row = orig_row
        for sw in switch_kws_2:
            if sw in row:
                print("Found key word --", sw, "row--", row)
                row = row.replace(sw, " ")
                sw_ctr2.add(sw)

        row = orig_row
        for sw in switch_kws_3:
            if sw in row:
                row = row.replace(sw, " ")
                print("Found key word --", sw, "row--", row)
                row_sw_ctr3.add(sw)
                sw_ctr_probables_1.add(sw)

        row = orig_row
        for sw in switch_kws_4:
            if sw in row:
                row = row.replace(sw, " ")
                print("Found key word --", sw, "row--", row)
                row_sw_ctr4.add(sw)
                sw_ctr_probables_2.add(sw)

        row = orig_row
        for sw in switch_kws_5:
            if sw in row:
                row = row.replace(sw, " ")
                print("Found key word --", sw, "row--", row)
                row_sw_ctr5.add(sw)
                sw_ctr_probables_1.add(sw)

        row = orig_row
        for sw in switch_kws:
            if sw in row:
                print("Found key word --", sw, "row--", row)
                row = row.replace(sw, " ")
                row_sw_ctr.add(sw)
                sw_ctr_probables_2.add(sw)
        if len(row_sw_ctr) > 0 and len(row_sw_ctr4) > 0:
            sw_ctr.update(row_sw_ctr)
            sw_ctr.update(row_sw_ctr4)

        if len(row_sw_ctr3) > 0 and len(row_sw_ctr5) > 0:
            sw_ctr3.update(row_sw_ctr3)
            sw_ctr3.update(row_sw_ctr5)

        row = orig_row
        for ct in counter_kws:
            if ct.lower() in row.lower():
                index = row.lower().find(ct.lower())
                if index != -1:
                    row = row[:index] + " " + row[index + len(ct):]
                print("Found key word --", ct)
                ctr_ctr.add(ct)

        row = orig_row
        for sw in not_counter_kws_1:
            if sw in row:
                print("Found key word --", sw)
                row = row.replace(sw, " ")
                non_ctr_ctr_1.append(sw)

    if len(ctr_ctr) >= 4 and len(non_ctr_ctr_1) <= 1:
        return 'COUNTER', len(ctr_ctr)
    elif len(ctr_ctr) >= 3 and len(non_ctr_ctr_1) == 0 and len(sw_ctr2) < 2:
        return 'COUNTER', len(ctr_ctr)
    elif len(sw_ctr) == 0 and len(ctr_ctr) > 1 and len(non_ctr_ctr_1) == 0 and len(sw_ctr2) < 2:
        return 'COUNTER', len(ctr_ctr)
    if len(sw_ctr2) + len(sw_ctr3) >= 3:
        return 'SWITCH', len(sw_ctr2) + len(sw_ctr3)
    elif len(sw_ctr2) >= 3:
        return 'SWITCH', len(sw_ctr2)
    elif len(ctr_ctr) == 0 and (len(sw_ctr2) > 2 or len(sw_ctr3) > 3 or len(sw_ctr) > 5):
        return 'SWITCH', len(sw_ctr2) + len(sw_ctr3) + len(sw_ctr)
    elif len(ctr_ctr) <= 1 and (
            len(sw_ctr_probables_1) > 3 or len(sw_ctr_probables_2) > 5) and contains_valid_switch_value(body):
        return 'SWITCH', len(sw_ctr_probables_1) + len(sw_ctr_probables_2)
    elif len(non_ctr_ctr_1) >= 3:
        return 'SWITCH', len(non_ctr_ctr_1)
    print('RETURN DEFAULT->', 'UNK', (len(sw_ctr) + len(sw_ctr2) + len(sw_ctr3) + len(ctr_ctr)))
    return 'UNK', (len(sw_ctr) + len(sw_ctr2) + len(sw_ctr3) + len(ctr_ctr))


def contains_word(key_wrd, text, mismatches_allowed=False, end=False):
    key_wrd = key_wrd.lower()
    text = text.lower()
    chars_len = len([c for c in list(key_wrd) if c.isalpha()])
    if not mismatches_allowed:
        if chars_len <= 4:
            mismatches_allowed = 0
        elif chars_len < 7:
            mismatches_allowed = 1
        else:
            mismatches_allowed = 2
    if end:
        reg_str = r"(" + key_wrd + r"$){e<=" + str(mismatches_allowed) + "}"
    else:
        reg_str = r"(" + key_wrd + r"){e<=" + str(mismatches_allowed) + "}"
    if not end:
        search_out = regex.search(reg_str, " " + text + " ")
    else:
        search_out = regex.search(reg_str, " " + text)
    if search_out:
        return True, search_out
    return False, 0


def contains_key_words(text, key_wrds=[], mismatches=[], end=False):
    text = " " + text.replace("\n", " ").lower() + " "
    if len(key_wrds) == 0:
        key_wrds = ["dispensed", "machine", "counter", "cassette", " date ", " increase ", "decrease", " out ",
                    "rejected",
                    " time ",
                    "remaining", " total ", " left ", " disp ", " tot ", " str ", " inc ", " dec ", " ic ", " dc ",
                    " oc ",
                    "record",
                    " pay", " card", "amount", " bal ", " bank ", " type ", "cleared", "last", "cleared", "date",
                    "bank", "time"]
    res = []
    for idx, key in enumerate(key_wrds):
        if len(mismatches) > 0:
            mis_allowed = mismatches[idx]
        else:
            mis_allowed = False
        if isinstance(key, str):
            word_search = contains_word(key, text, mis_allowed, end)
            if word_search[0]:
                print("Found match", word_search[1], "key--", key)
                res.append(word_search[1])
        else:
            full_word_search = contains_word(" ".join(key), text, mis_allowed, end)
            if full_word_search[0]:
                contains_all_words = True
                for word in key:
                    if not contains_word(word, full_word_search[1].group(), mis_allowed, end)[0]:
                        contains_all_words = False
                        break
                if contains_all_words:
                    print("Found match", full_word_search[1], "key--", key)
                    res.append(full_word_search[1])
    if len(res) > 0:
        return res
    return False


def process_pts(coords):
    [x, y, w, h] = coords
    return [x, y, x + w, y + h]


def decoder_output_to_text(ctcOutput, batchSize, charList):
    encodedLabelStrs = [[] for i in range(batchSize)]
    decoded = ctcOutput[0][0]
    idxDict = {b: [] for b in range(batchSize)}
    for (idx, idx2d) in enumerate(decoded.indices):
        label = decoded.values[idx]
        batchElement = idx2d[0]  # index according to [b,t]
        encodedLabelStrs[batchElement].append(label)
    return [str().join([charList[c] for c in labelStr]) for labelStr in encodedLabelStrs]


def get_texts(lines, text_blocks, ocr_model, batch_size, max_text_len, charList, imgSize, img):
    texts_obj = {}
    loader = DataLoader(text_blocks, batch_size, imgSize, img)
    print("Total samples", len(loader.samples))

    while loader.hasNext():
        iterInfo = loader.getIteratorInfo()
        print('Batch:', iterInfo[0], '/', iterInfo[1])
        batch = loader.getNext()
        numBatchElements = len(batch.imgs)
        rnn_out = ocr_model.predict_on_batch(batch.imgs)
        decoded = tf.compat.v1.nn.ctc_greedy_decoder(inputs=rnn_out, sequence_length=[max_text_len] * numBatchElements)
        recognized = decoder_output_to_text(decoded, numBatchElements, charList)
        # print(recognized)
        for id, text in zip(batch.ids, recognized):
            texts_obj[id] = text
            # print("ID---",id,"TEXT---",text)

    for line_idx, line in enumerate(lines):
        for block_idx, block in enumerate(line):
            id = block["id"]
            lines[line_idx][block_idx]["text"] = texts_obj[id]
            lines[line_idx][block_idx]["pts"] = process_pts(lines[line_idx][block_idx]["pts"])
            lines[line_idx][block_idx].pop('minAreaRect', None)

    return lines


def get_orientation_slip_type(img_path):
    gc.collect()
    deskew_res = deskew(img_path)
    cropped_img = deskew_res['cropped']

    for orientation in [0, 180, 90, -90]:
        logging.debug("orientation -" + str(orientation))
        if orientation in [180, 90, -90]:
            deskew_img = imutils.rotate_bound(cropped_img, orientation)
        else:
            deskew_img = cropped_img
        st_time = time.time()
        detect_text_res = TextDetection(img=deskew_img, path=img_path, cls_model=classify_model, debug=False)
        td_time = time.time() - st_time
        logging.debug("Time taken for text detection " + str(td_time))
        img = detect_text_res.oriented_orig_img
        [h, w] = img.shape[:2]
        print("height", h, "width", w)
        im_out = img.copy()
        lines = detect_text_res.lines
        text_blocks = []
        color_1 = [0, 0, 255]
        color_2 = [0, 255, 0]
        color_3 = [255, 0, 0]
        curr_color = color_1
        for line in lines:
            if curr_color == color_1:
                curr_color = color_2
            elif curr_color == color_2:
                curr_color = color_3
            else:
                curr_color = color_1
            for block in line:
                [x, y, w, h] = block["pts"]
                cv2.rectangle(im_out, (x, y), (x + w, y + h), curr_color, 2)
                text_blocks.append(block)
        max_txt_len = 256
        lines = get_texts(lines, text_blocks, ocr_model, 32, max_txt_len, charlist, IMG_SIZE,
                          detect_text_res.oriented_orig_gray.copy())
        detect_text_res.lines = lines

        full_text, line_ll_ = "", []
        for line in detect_text_res.lines:
            line_txt, locarr_ = "", []
            if curr_color == color_1:
                curr_color = color_2
            elif curr_color == color_2:
                curr_color = color_3
            else:
                curr_color = color_1
            for block in line:
                [x1, y1, x2, y2] = block["pts"]
                line_txt = line_txt + " " + block["text"]
                locarr_.append(block)
            line_ll_.append(locarr_)
            full_text = full_text + line_txt + "\n"

        inverted_slip_kws = ['TVIO', '03SNJdSI0', 'DNINIV', 'ONINIV']  # some keywords that appear in inverted slips
        slip_type_found, bkp = decide_slip_type(full_text)
        if 'UNK' not in slip_type_found and not contains_key_words(full_text, inverted_slip_kws,
                                                                   [0] * len(inverted_slip_kws)):
            return orientation, slip_type_found
        elif orientation in [90, 180, -90]:
            other_kw_search = contains_key_words(full_text, other_kws)
            if other_kw_search and len(other_kw_search) > 1:
                return orientation, slip_type_found
        if orientation == 0:
            other_kw_search = contains_key_words(full_text, other_kws)
            if other_kw_search and len(other_kw_search) > 1:
                return orientation, slip_type_found
