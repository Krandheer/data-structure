"""
get orientation will give me slip type and angle by which deskew image needs to be rotated
"""
import imutils

from google_ocr.get_orientation import get_orientation_slip_type
from utils.deskew_method import deskew

import cv2
import numpy as np
from glob import glob
import os


def concatenate_image(image_folder, image_id, out_path):
    image_folder = image_folder
    image_id = f'{image_id}*'
    temp = os.path.join(os.path.expanduser("~"), 'Downloads', image_folder)
    image_paths = glob(os.path.join(temp, image_id))
    path1, path2, path3, path4 = (), (), (), ()

    for path in image_paths:
        orientation, slip_type = get_orientation_slip_type(path)
        if slip_type == "SWITCH":
            if 'SA' in path or 'CA' in path:
                path3 = orientation, path
            else:
                path4 = orientation, path

        # need to test for counter in python console
        elif slip_type == "COUNTER":
            if "CA" in path or "SA" in path:
                path1 = orientation, path
            else:
                path2 = orientation, path

    images = [path1, path2, path3, path4]

    processed_image = []

    w, h = deskew(path1)['cropped'].shape[:2][1], deskew(path1)['cropped'].shape[:2][1]
    for orientation, img in images:
        deskew_res = deskew(img)
        cropped_image = deskew_res['cropped']
        cropped_image = imutils.rotate_bound(cropped_image, orientation)
        cropped_image = cv2.resize(cropped_image, (w, h))
        processed_image.append(cropped_image)

    # Concatenate the two images horizontally
    result1 = np.concatenate((processed_image[0], processed_image[1]), axis=1)
    result2 = np.concatenate((processed_image[2], processed_image[3]), axis=1)

    result = np.concatenate((result1, result2), axis=0)
    # Save the resulting image
    cv2.imwrite(f'{out_path}/{image_id[:-1]}.jpg', result)
