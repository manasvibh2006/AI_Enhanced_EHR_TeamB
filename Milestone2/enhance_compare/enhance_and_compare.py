# import cv2
# import numpy as np
# import os

# def enhance_xray(img):
#     # 1. Denoising
#     denoised = cv2.fastNlMeansDenoising(img, None, h=10)

#     # 2. CLAHE for contrast enhancement
#     clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
#     clahe_img = clahe.apply(denoised)

#     # 3. Sharpening
#     kernel = np.array([[0, -1, 0],
#                        [-1, 5, -1],
#                        [0, -1, 0]])
#     sharpened = cv2.filter2D(clahe_img, -1, kernel)

#     return sharpened


# def save_comparison(original, enhanced, save_path):
#     o = cv2.cvtColor(original, cv2.COLOR_GRAY2BGR)
#     e = cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)
#     combined = np.hstack((o, e))
#     cv2.imwrite(save_path, combined)


# if __name__ == "__main__":
#     input_folder = "data/raw/"
#     enhanced_folder = "outputs/enhanced/"
#     comparison_folder = "outputs/comparisons/"

#     os.makedirs(enhanced_folder, exist_ok=True)
#     os.makedirs(comparison_folder, exist_ok=True)

#     supported_ext = [".jpg", ".jpeg", ".png"]

#     for file_name in os.listdir(input_folder):
#         if any(file_name.lower().endswith(ext) for ext in supported_ext):

#             image_path = os.path.join(input_folder, file_name)
#             print(f"Enhancing: {file_name}")

#             img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#             enhanced = enhance_xray(img)

#             enhanced_path = os.path.join(enhanced_folder, f"enh_{file_name}.png")
#             comparison_path = os.path.join(comparison_folder, f"comp_{file_name}.png")

#             cv2.imwrite(enhanced_path, enhanced)
#             save_comparison(img, enhanced, comparison_path)

#     print("✔ All images enhanced successfully!")

