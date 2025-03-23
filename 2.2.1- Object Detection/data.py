import cv2
import numpy as np
import random
import glob
import os

def add_fog(image):
    overlay = np.full(image.shape, 255, dtype=np.uint8)
    alpha = random.uniform(0.3, 0.6)  # Adjust fog intensity
    foggy_image = cv2.addWeighted(image, 1 - alpha, overlay, alpha, 0)
    return foggy_image

def add_rain(image):
    rain_layer = np.zeros_like(image, dtype=np.uint8)
    num_drops = random.randint(500, 1000)
    for _ in range(num_drops):
        x, y = random.randint(0, image.shape[1] - 1), random.randint(0, image.shape[0] - 1)
        cv2.line(rain_layer, (x, y), (x+2, y+10), (200, 200, 200), 1)
    rain_image = cv2.addWeighted(image, 0.8, rain_layer, 0.2, 0)
    return rain_image

# Input dataset directory
image_paths = glob.glob(r"C:\Users\Asus\Desktop\BDD100K\train\*.jpg")

# Output directory
output_dir = r"C:\Users\Asus\Desktop\BDD100K\foggy_rain"
os.makedirs(output_dir, exist_ok=True)
for img_path in image_paths[:500]:  # Limit to 500 images for training
    image = cv2.imread(img_path)

    if image is None:
        print(f"Skipping: {img_path} (could not load)")
        continue

    # Apply fog and rain effects
    foggy = add_fog(image)
    rainy = add_rain(image)

    # Extract filename and create new paths
    filename = os.path.basename(img_path)  # Example: 'image1.jpg'
    foggy_path = os.path.join(output_dir, filename.replace(".jpg", "_foggy.jpg"))
    rainy_path = os.path.join(output_dir, filename.replace(".jpg", "_rainy.jpg"))

    # Save images with corrected paths
    cv2.imwrite(foggy_path, foggy)
    cv2.imwrite(rainy_path, rainy)

    print(f"Processed: {filename}")

print("Dataset augmentation complete!")
