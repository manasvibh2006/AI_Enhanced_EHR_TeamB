import cv2
import os
import numpy as np
from shutil import copy2

INPUT_FOLDER = r"Milestone1\DATA\Medical_Imaging_Data\Xray"  

OUTPUT_FOLDER = "low_quality_sample/"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def blur_score(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

def brightness_score(image):
    return np.mean(image)

def contrast_score(image):
    return image.std()

def noise_score(image):
    return cv2.mean(cv2.absdiff(image, cv2.GaussianBlur(image, (3,3), 0)))[0]

quality_list = []

for img_name in os.listdir(INPUT_FOLDER):
    path = os.path.join(INPUT_FOLDER, img_name)
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        continue

    b = blur_score(image)
    br = brightness_score(image)
    c = contrast_score(image)
    n = noise_score(image)

    score = (0.4*b) + (0.2*br) + (0.2*c) - (0.2*n)
    
    quality_list.append((score, img_name))

quality_list.sort(key=lambda x: x[0])

for score, img_name in quality_list[:25]:
    copy2(os.path.join(INPUT_FOLDER, img_name), OUTPUT_FOLDER)

print("Low-quality images copied to:", OUTPUT_FOLDER)
