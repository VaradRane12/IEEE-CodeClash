import cv2
import torch
import matplotlib.pyplot as plt
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")  # Using YOLOv8 nano model

# Function to perform object detection and return the image with bounding boxes
def detect_objects(image_path):
    img = cv2.imread(image_path)  # Load image
    results = model(img)  # Perform YOLO inference

    # Draw bounding boxes
    for box in results[0].boxes.xyxy.cpu().numpy():
        x1, y1, x2, y2 = map(int, box[:4])
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)  # Green bounding box

    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB for display

# Image paths (replace with actual file paths)
no_fog_img_path = r"C:\Users\Asus\Desktop\Foggy_Cityscapes\No_Fog\\123.png"
medium_fog_img_path = r"C:\Users\Asus\Desktop\Foggy_Cityscapes\Medium_Fog\\123.png"
dense_fog_img_path = r"C:\Users\Asus\Desktop\Foggy_Cityscapes\Dense_Fog\\123.png"

# Run detection on each image
no_fog_detected = detect_objects(no_fog_img_path)
medium_fog_detected = detect_objects(medium_fog_img_path)
dense_fog_detected = detect_objects(dense_fog_img_path)

# Display results side by side
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(no_fog_detected)
plt.title("No Fog")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(medium_fog_detected)
plt.title("Medium Fog")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(dense_fog_detected)
plt.title("Dense Fog")
plt.axis("off")

plt.show()
