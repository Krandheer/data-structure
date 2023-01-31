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
            prev_x_max = 0
            prev_y_max = 0
            for row in temp:
                row_contour = row['pts']
                row_y = [vertex[1] for vertex in row_contour]
                row_x = [vertex[0] for vertex in row_contour]
                if prev_x_max < max(row_x):
                    prev_x_max = max(row_x)
                if prev_y_max < max(row_y):
                    prev_y_max = max(row_y)

        current_contour = text['bounding_box']
        current_y_coords = [vertex[1] for vertex in current_contour]
        current_y_min = min(current_y_coords)
        current_y_max = max(current_y_coords)
        current_x_max = max([vertex[0] for vertex in current_contour])

        added = False
        if current_x_max < w and current_y_max < h:
            for rows in counter1:
                min_x = 0
                if rows and rows[0]['pts']:
                    for row in rows:
                        row_contour = row['pts']
                        row_y = [vertex[1] for vertex in row_contour]
                        row_x = [vertex[0] for vertex in row_contour]
                        if min_x > min(row_x):
                            min_x = min(row_x)
                        if max(row_y) - 11 <= current_y_max <= max(row_y) + 11 and min(
                                row_y) - 11 <= current_y_min <= min(row_y) + 10 and min_x < current_x_max:
                            rows.append({"text": description, 'pts': contour})
                            added = True
                            break
                if added:
                    break

        elif current_x_max > w and current_y_max < h:
            for rows in counter2:
                min_x = 0
                if rows and rows[0]['pts']:
                    for row in rows:
                        row_contour = row['pts']
                        row_y = [vertex[1] for vertex in row_contour]
                        row_x = [vertex[0] for vertex in row_contour]
                        if min_x > min(row_x):
                            min_x = min(row_x)
                        if max(row_y) - 11 <= current_y_max <= max(row_y) + 11 and min(
                                row_y) - 11 <= current_y_min <= min(row_y) + 10 and min_x < current_x_max:
                            rows.append({"text": description, 'pts': contour})
                            added = True
                            break
                if added:
                    break

        elif current_x_max < w and current_y_max > h:
            for rows in switch1:
                min_x = 0
                if rows and rows[0]['pts']:
                    for row in rows:
                        row_contour = row['pts']
                        row_y = [vertex[1] for vertex in row_contour]
                        row_x = [vertex[0] for vertex in row_contour]
                        if min_x > min(row_x):
                            min_x = min(row_x)
                        if max(row_y) - 11 <= current_y_max <= max(row_y) + 11 and min(
                                row_y) - 11 <= current_y_min <= min(row_y) + 10 and min_x < current_x_max:
                            rows.append({"text": description, 'pts': contour})
                            added = True
                            break
                if added:
                    break

        elif current_x_max > w and current_x_max > h:
            for rows in switch2:
                min_x = 0
                if rows and rows[0]['pts']:
                    for row in rows:
                        row_contour = row['pts']
                        row_y = [vertex[1] for vertex in row_contour]
                        row_x = [vertex[0] for vertex in row_contour]
                        if min_x > min(row_x):
                            min_x = min(row_x)
                        if max(row_y) - 11 <= current_y_max <= max(row_y) + 11 and min(
                                row_y) - 11 <= current_y_min <= min(row_y) + 10 and min_x < current_x_max:
                            rows.append({"text": description, 'pts': contour})
                            added = True
                            break
                if added:
                    break

        # prev_y_min should come from temp, as here I'm deciding if it should go in current temp or not,
        start_new_temp = True
        if not added:
            min_x = 0
            for row in temp:
                row_contour = row['pts']
                row_y = [vertex[1] for vertex in row_contour]
                row_x = [vertex[0] for vertex in row_contour]
                if min_x > min(row_x):
                    min_x = min(row_x)
                if max(row_y) - 11 <= current_y_max <= max(row_y) + 11 and min_x < current_x_max:
                    temp.append({"text": description, 'pts': contour})
                    start_new_temp = False
                    break
            # here prev_countour should come from temp values, and max and min values of y and h
            # if index == 0 then keep prev counter same, else get it from temp

            if start_new_temp:
                # counter 1 value formation
                if prev_x_max < w and prev_y_max < h:
                    if index == 0:
                        counter1.append([{"text": description, 'pts': contour}])
                    else:
                        counter1.append(temp)
                        temp = [{"text": description, 'pts': contour}]

                # counter 2 value formation
                elif prev_x_max > w and prev_y_max < h:
                    counter2.append(temp)
                    temp = [{"text": description, 'pts': contour}]

                # switch 1 value formation
                elif prev_x_max < w and prev_y_max > h:
                    switch1.append(temp)
                    temp = [{"text": description, 'pts': contour}]

                # switch 2 value formation
                elif prev_x_max > w and prev_y_max > h:
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
    print({'ocr_opt': ocr_opt})
    return ocr_opt
    # with open(ocr_output_path, "w") as f:
    #     json.dump({'ocr_opt': ocr_opt}, f)


get_image_ocr_data("result.jpg", 'ocr.json')
