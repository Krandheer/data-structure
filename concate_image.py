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

image_folder = "s1cn"
image_id = 'S1CNE385*'
temp = os.path.join(os.path.expanduser("~"), 'Downloads', image_folder)
image_paths = glob(os.path.join(temp, image_id))
path1, path2, path3, path4 = '', '', '', ''
# for path in image_paths:
#     if "SA" in path:
#         path3 = path
#     elif "SB" in path:
#         path4 = path
#     elif "CA" in path:
#         path1 = path
#     else:
#         path2 = path
images = []

for path in image_paths:
    orientation, slip_type = get_orientation_slip_type(path)
    if slip_type == "SWITCH":
        if 'SA' in path or 'CA' in path:
            path3 = path
            images.append((orientation, path3))
        else:
            path4 = path
            images.append((orientation, path4))

    # need to test for counter in python console
    elif slip_type == "COUNTER":
        if "CA" in path or "SA" in path:
            path1 = path
            images.append((orientation, path1))
        else:
            path2 = path
            images.append((orientation, path2))
sorted_image = sorted(images, key=lambda val: val[1])

processed_image = []

w, h = deskew(path1)['cropped'].shape[:2][1], deskew(path1)['cropped'].shape[:2][1]
for orientation, img in sorted_image:
    deskew_res = deskew(img)
    cropped_image = deskew_res['cropped']
    cropped_image = imutils.rotate_bound(cropped_image, orientation)
    cropped_image = cv2.resize(cropped_image, (w, h))
    processed_image.append(cropped_image)

# Concatenate the two images horizontally
result1 = np.concatenate((processed_image[0], processed_image[1]), axis=1)
result2 = np.concatenate((processed_image[2], processed_image[3]), axis=1)

result = np.concatenate((result1, result2), axis=0)
x, y, _ = result.shape
print(f"result x3: {y}, 3: {x}")
# Save the resulting image
cv2.imwrite("result.jpg", result)
