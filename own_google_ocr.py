import io
import json
import os

import cv2
from google.cloud import vision

basepath = os.path.dirname(__file__)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(basepath, 'ocr_credentials.json')
os.environ["GCLOUD_PROJECT"] = "My First Project"


def extract_texts(image_path, texts):
    """
    Height difference is coming to be 20 approx for date at least. If x is increasing and height difference is not
    more than 30 then consider same row. If x decrease then starting of new row. When indication of another row then
    create another list and put things in that list. Already have set of 4 list of list on basis of coordinate for
    each slip
    """
    image = cv2.imread(image_path)
    h, w = image.shape[:2]
    h, w = h // 2, w // 2
    counter1 = []
    counter2 = []
    switch1 = []
    switch2 = []
    temp = []
    for index, text in enumerate(texts[1:]):
        "get text and add in it's list"
        description = text['text']
        contour = text['bounding_box']

        if index == 0:
            prev_contour = text['bounding_box']
            prev_y_coords = [vertex[1] for vertex in prev_contour]
            prev_y_min = min(prev_y_coords)
            prev_y_max = max(prev_y_coords)
            prev_x_max = max([vertex[0] for vertex in prev_contour])
        else:
            prev_contour = texts[index - 1]['bounding_box']
            prev_y_coords = [vertex[1] for vertex in prev_contour]
            prev_y_min = min(prev_y_coords)
            prev_y_max = max(prev_y_coords)
            prev_x_max = max([vertex[0] for vertex in prev_contour])

        current_contour = text['bounding_box']
        current_y_coords = [vertex[1] for vertex in current_contour]
        current_y_min = min(current_y_coords)
        current_y_max = max(current_y_coords)
        current_x_max = max([vertex[0] for vertex in current_contour])

        added = False
        if current_x_max < w and current_y_max < h:
            for row in counter1:
                if row and row[0]['pts']:
                    row_contour = row[0]['pts']
                    row_y = [vertex[1] for vertex in row_contour]
                    # to check in same row we need to use y coordinate
                    if max(row_y) - 8 < current_y_max < max(row_y) + 8:
                        row.append({"text": description, 'pts': contour})
                        added = True
                        break

        elif current_x_max > w and current_y_max < h:
            for row in counter2:
                if row and row[0]['pts']:
                    row_contour = row[0]['pts']
                    row_y = [vertex[1] for vertex in row_contour]
                    # to check in same row we need to use y coordinate
                    if max(row_y) - 8 < current_y_max < max(row_y) + 8:
                        row.append({"text": description, 'pts': contour})
                        added = True
                        break

        elif current_x_max < w and current_y_max > h:
            for row in switch1:
                if row and row[0]['pts']:
                    row_contour = row[0]['pts']
                    row_y = [vertex[1] for vertex in row_contour]
                    # to check in same row we need to use y coordinate
                    if max(row_y) - 8 < current_y_max < max(row_y) + 8:
                        row.append({"text": description, 'pts': contour})
                        added = True
                        break

        elif current_x_max > w and current_x_max > h:
            for row in switch2:
                if row and row[0]['pts']:
                    row_contour = row[0]['pts']
                    row_y = [vertex[1] for vertex in row_contour]
                    # to check in same row we need to use y coordinate
                    if max(row_y) - 8 < current_y_max < max(row_y) + 8:
                        row.append({"text": description, 'pts': contour})
                        added = True
                        break

        if not added:
            if prev_y_min + 8 >= current_y_min >= prev_y_min - 8 and prev_y_max - 8 <= current_y_max <= prev_y_max + 8 and prev_x_max < current_x_max:
                temp.append({"text": description, 'pts': contour})

            # coming here means next row is starting
            elif prev_contour[-1][0] < w and prev_contour[-1][1] < h or index == 0:
                counter1.append(temp)
                temp = [{"text": description, 'pts': contour}]

            elif prev_contour[-1][0] > w and prev_contour[-1][1] < h:
                counter2.append(temp)
                temp = [{"text": description, 'pts': contour}]

            elif prev_contour[-1][0] < w and prev_contour[-1][1] > h:
                switch1.append(temp)
                temp = [{"text": description, 'pts': contour}]

            elif prev_contour[-1][0] > w and prev_contour[-1][1] > h:
                switch2.append(temp)
                temp = [{"text": description, 'pts': contour}]
    result = {'Counter1': counter1, 'Counter2': counter2, "Switch1": switch1, "Switch2": switch2}
    return result


def get_image_ocr_data(image_path, ocr_output_path):
    """
    I can get the image dimension here and I know image of same size so half of widht is starting of new image in same
    row and half of height is starting of 2nd row of concatenated image
    """

    client = vision.ImageAnnotatorClient()
    image_location = image_path
    with open(image_location, 'rb') as img:
        content = img.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)

    text_data = []
    for annotation in response.text_annotations:
        text_data.append({
            'text': annotation.description,
            'bounding_box': [(vertex.x, vertex.y) for vertex in annotation.bounding_poly.vertices]
        })

    ocr_opt = extract_texts(image_path, text_data)
    print(ocr_opt)
    with open(ocr_output_path, "w") as f:
        json.dump({'ocr_opt': ocr_opt}, f)


get_image_ocr_data("S1AWTX12.jpg", 'ocr.json')