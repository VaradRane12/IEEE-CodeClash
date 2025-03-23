from glob import glob
import cv2
import numpy as np
import os
from ultralytics import YOLO

# Function to enhance contrast using CLAHE (Contrast Limited Adaptive Histogram Equalization)
def enhance_contrast(img):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    l = clahe.apply(l)
    lab = cv2.merge((l, a, b))
    return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

# Function to calculate Intersection over Union (IoU) between two bounding boxes
def calculate_iou(box1, box2):
    x1, y1, x2, y2 = box1  # Unpack first bounding box
    x1g, y1g, x2g, y2g = box2  # Unpack second bounding box
    
    # Calculate intersection coordinates
    xi1 = max(x1, x1g)
    yi1 = max(y1, y1g)
    xi2 = min(x2, x2g)
    yi2 = min(y2, y2g)
    
    # Calculate intersection area
    inter_area = max(0, xi2 - xi1) * max(0, yi2 - yi1)
    
    # Calculate areas of individual bounding boxes
    box1_area = (x2 - x1) * (y2 - y1)
    box2_area = (x2g - x1g) * (y2g - y1g)
    
    # Calculate union area
    union_area = box1_area + box2_area - inter_area
    
    # Compute IoU, return 0 if union area is zero
    return inter_area / union_area if union_area else 0

# Function to run YOLO object detection on an image
def run_detection(model, img):
    results = model(img)  # Run model inference
    return results[0].boxes.xyxy.cpu().numpy()  # Extract bounding boxes

# Load YOLO model
model = YOLO("yolov8n.pt")

# Define dataset directories
base_dir = "C:\\Users\\Asus\\Desktop\\Foggy_Cityscapes"
no_fog_dir = os.path.join(base_dir, "No_Fog")
medium_fog_dir = os.path.join(base_dir, "Medium_Fog")
dense_fog_dir = os.path.join(base_dir, "Dense_Fog")

# Get sorted list of images from each directory
no_fog_images = sorted(glob(os.path.join(no_fog_dir, "*.png")))
medium_fog_images = sorted(glob(os.path.join(medium_fog_dir, "*.png")))
dense_fog_images = sorted(glob(os.path.join(dense_fog_dir, "*.png")))

iou_scores = []  # Store IoU scores
count = 0  # Initialize counter

# Loop through images in all three categories
for no_fog_img, med_fog_img, dense_fog_img in zip(no_fog_images, medium_fog_images, dense_fog_images):

    
    # Read images
    med_fog = cv2.imread(med_fog_img)
    dense_fog = cv2.imread(dense_fog_img)
    
    # Enhance contrast in foggy images
    enhanced_med_fog = enhance_contrast(med_fog)
    enhanced_dense_fog = enhance_contrast(dense_fog)
    
    # Run YOLO object detection
    no_fog_boxes = run_detection(model, no_fog_img)
    med_fog_boxes = run_detection(model, enhanced_med_fog)
    dense_fog_boxes = run_detection(model, enhanced_dense_fog)
    
    # Compute IoU for each detected object
    for n_box in no_fog_boxes:
        max_iou_med = max([calculate_iou(n_box, f_box) for f_box in med_fog_boxes] or [0])
        max_iou_dense = max([calculate_iou(n_box, f_box) for f_box in dense_fog_boxes] or [0])
        iou_scores.append((max_iou_med, max_iou_dense))
        
    count+=1
    if count == 10:
        break

# Calculate average IoU values
iou_avg_med = np.mean([iou[0] for iou in iou_scores])
iou_avg_dense = np.mean([iou[1] for iou in iou_scores])

# Print results
print(f"Average IoU for Medium Fog: {iou_avg_med:.4f}")
print(f"Average IoU for Dense Fog: {iou_avg_dense:.4f}")
