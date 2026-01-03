import cv2
import numpy as np
import os
from tqdm import tqdm

print("🔄 Processing your 001.jpeg, 002.jpeg, 003.jpeg...")
os.makedirs('enhanced', exist_ok=True)

raw_files = [f for f in os.listdir('raw') if f.lower().endswith(('.jpg','.jpeg','.png'))]
print(f"Found {len(raw_files)} images")

success = 0
for img_file in tqdm(raw_files, desc="Enhancing 001→030"):
    img_path = f'raw/{img_file}'
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    
    if img is not None:
        # Fix white rectangles: Denoise + CLAHE + Sharpen
        denoised = cv2.fastNlMeansDenoising(img, h=10)
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        enhanced = clahe.apply(denoised)
        cv2.imwrite(f'enhanced/{img_file}', enhanced)
        success += 1

print(f"\n✅ SUCCESS: {success}/{len(raw_files)} enhanced!")
print("📁 Check: dir enhanced")
