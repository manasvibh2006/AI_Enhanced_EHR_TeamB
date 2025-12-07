import cv2
import os
import numpy as np

# ----------------- Folders ----------------- #

INPUT_FOLDER = r"C:\Users\Manasvi\OneDrive\Desktop\AI Enhanced ehr - final1\AI_Enhanced_EHR_TeamB\Milestone2\low_quality_sample"
ENHANCED_FOLDER = r"milestone2_outputs/enhanced/"
COMPARISON_FOLDER = r"milestone2_outputs/comparisons/"

os.makedirs(ENHANCED_FOLDER, exist_ok=True)
os.makedirs(COMPARISON_FOLDER, exist_ok=True)

# ----------------- Enhancement Functions ----------------- #

def denoise(image):
    return cv2.GaussianBlur(image, (3,3), 0)

def sharpen(image):
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)

def clahe_enhancement(image):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    return clahe.apply(image)

def upscale(image):
    return cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

# ----------------- Processing Loop ----------------- #

for img_name in os.listdir(INPUT_FOLDER):
    path = os.path.join(INPUT_FOLDER, img_name)
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        continue

    # Enhancement steps
    den = denoise(image)
    sharp = sharpen(den)
    clahe_img = clahe_enhancement(sharp)
    upscaled = upscale(clahe_img)

    # Save enhanced image
    cv2.imwrite(os.path.join(ENHANCED_FOLDER, img_name), upscaled)

    # ----------------- Create Comparison Image ----------------- #

    # Resize original to match enhanced for side-by-side
    original_resized = cv2.resize(image, (upscaled.shape[1], upscaled.shape[0]))

    # Side-by-side comparison
    comparison = cv2.hconcat([original_resized, upscaled])

    # Save comparison
    cv2.imwrite(os.path.join(COMPARISON_FOLDER, img_name), comparison)

print("Enhancement + Comparison generation completed!")
