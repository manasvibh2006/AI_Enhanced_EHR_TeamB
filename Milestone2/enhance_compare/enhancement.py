import cv2
import os
import numpy as np

INPUT_FOLDER = r"data/raw/"
OUTPUT_FOLDER = r"enhanced_output/"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def denoise(image):
    """Noise Reduction (Gaussian Filter)"""
    return cv2.GaussianBlur(image, (3,3), 0)

def sharpen(image):
    """Sharpening Using Kernel"""
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)

def clahe_enhancement(image):
    """Contrast Enhancement using CLAHE"""
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    return clahe.apply(image)

def upscale(image):
    """Simple resolution improvement"""
    return cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

# ------- PROCESSING LOOP -------- #

for img_name in os.listdir(INPUT_FOLDER):
    path = os.path.join(INPUT_FOLDER, img_name)

    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        continue

    # Steps
    den = denoise(image)
    sharp = sharpen(den)
    clahe_img = clahe_enhancement(sharp)
    upscaled = upscale(clahe_img)

    # Save final enhanced image
    cv2.imwrite(os.path.join(OUTPUT_FOLDER, img_name), upscaled)

print("All images enhanced and saved to:", OUTPUT_FOLDER)
