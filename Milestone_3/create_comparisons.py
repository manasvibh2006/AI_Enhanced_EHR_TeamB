import cv2
import matplotlib
matplotlib.use('Agg')  # FIX: Non-interactive backend
import matplotlib.pyplot as plt
import os
from tqdm import tqdm

print("🔄 Creating comparisons (FIXED)...")
os.makedirs('comparisons', exist_ok=True)

raw_files = [f for f in os.listdir('raw') if f.lower().endswith('.jpeg')]
print(f"Found {len(raw_files)} images")

success = 0
for i, img_file in enumerate(tqdm(raw_files, desc="Comparisons")):
    orig = cv2.imread(f'raw/{img_file}', 0)
    enh = cv2.imread(f'enhanced/{img_file}', 0)
    
    if orig is None or enh is None:
        print(f"❌ Skip {img_file}")
        continue
    
    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.imshow(orig, cmap='gray')
    ax1.set_title('Original')
    ax1.axis('off')
    ax2.imshow(enh, cmap='gray')
    ax2.set_title('Enhanced')
    ax2.axis('off')
    
    # SAVE with explicit close
    comp_path = f'comparisons/comp_{i+1:03d}.png'
    plt.savefig(comp_path, dpi=150, bbox_inches='tight', pad_inches=0.1)
    plt.close(fig)  # CRITICAL: Close figure
    success += 1

print(f"\n✅ {success} PNGs saved to comparisons/")
print("📁 VERIFY:")
import os
print(f"Files in comparisons/: {len([f for f in os.listdir('comparisons')])}")
