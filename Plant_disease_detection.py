import cv2
import numpy as np


def detect_disease_simple(image_path):
    try:
        img = cv2.imread(image_path)
        if img is None:
            return "Error: Image not found"
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lower_bound = np.array([0, 0, 100])
        upper_bound = np.array([100, 255, 255])

        mask = cv2.inRange(hsv, lower_bound, upper_bound)

        green_pixels = cv2.countNonZero(mask)
        total_pixels = img.shape[0] * img.shape[1]
        green_percentage = (green_pixels / total_pixels) * 100

        if green_percentage > 50:
            return "Healthy"
        else:
            return "Diseased"

    except Exception as e:
        print(f"Error: {e}")
        return "Error"


image_paths = ['static/img/img1.jpg',
               'static/img/img2.jpg',
               'static/img/img3.jpg']

for image_path in image_paths:
    result = detect_disease_simple(image_path)
    print(f" Predicted Disease: {result}")
