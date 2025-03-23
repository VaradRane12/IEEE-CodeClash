import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to enhance contrast using CLAHE
def enhance_contrast(img):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    l = clahe.apply(l)
    lab = cv2.merge((l, a, b))
    return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

# Load foggy image
image_path = r"C:\Users\Asus\Desktop\Foggy_Cityscapes\Dense_Fog\\004.png"  # Replace with your image path
foggy_img = cv2.imread(image_path)

# Enhance contrast
enhanced_img = enhance_contrast(foggy_img)

# Convert images from BGR to RGB for displaying with Matplotlib
foggy_img_rgb = cv2.cvtColor(foggy_img, cv2.COLOR_BGR2RGB)
enhanced_img_rgb = cv2.cvtColor(enhanced_img, cv2.COLOR_BGR2RGB)

# Display original and enhanced images side by side
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(foggy_img_rgb)
plt.title("Original Foggy Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(enhanced_img_rgb)
plt.title("Contrast-Enhanced Image")
plt.axis("off")

plt.show()
