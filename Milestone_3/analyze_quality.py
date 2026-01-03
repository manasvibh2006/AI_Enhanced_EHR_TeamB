import cv2
import numpy as np
import os
import pandas as pd

def analyze_image_quality(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return {'filename': os.path.basename(img_path), 'issues': 'Cannot read image'}
    
    brightness = img.mean()
    contrast = img.std()
    laplacian_var = cv2.Laplacian(img, cv2.CV_64F).var()
    
    issues = []
    if brightness < 80: issues.append('Low Brightness')
    if contrast < 35: issues.append('Low Contrast')
    if laplacian_var < 100: issues.append('Blurred')
    
    return {
        'filename': os.path.basename(img_path),
        'brightness': round(brightness, 2),
        'contrast': round(contrast, 2),
        'blur_score': round(laplacian_var, 2),
        'issues': ', '.join(issues) if issues else 'Good quality'
    }

print("🔍 Scanning raw/ folder...")
raw_files = [f for f in os.listdir('raw') if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

print(f"✅ Found {len(raw_files)} images")

results = []
for img_file in raw_files:
    print(f"Analyzing {img_file}...")
    try:
        result = analyze_image_quality(f'raw/{img_file}')
        results.append(result)
    except Exception as e:
        results.append({'filename': img_file, 'issues': f'Error: {str(e)}'})

df = pd.DataFrame(results)
df.to_csv('quality_analysis.csv', index=False)

print("\n📊 QUALITY ANALYSIS RESULTS (First 10):")
print(df[['filename', 'issues']].head(10).to_string(index=False))
print(f"\n💾 Saved quality_analysis.csv ({len(results)} images analyzed)")
print("\n🎉 Step 2 COMPLETE! Next: python enhance_images.py")
