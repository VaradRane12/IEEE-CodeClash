from glob import glob
import cv2
import numpy as np
import os
from ultralytics import YOLO

def enhance_contrast(img):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    l = clahe.apply(l)
    lab = cv2.merge((l, a, b))
    return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

def draw_boxes(img, boxes, color=(0, 255, 0), label=""):
    for box in boxes:
        x1, y1, x2, y2 = map(int, box)
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
    cv2.putText(img, label, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    return img

def run_detection(model, img):
    results = model(img)
    return results[0].boxes.xyxy.cpu().numpy()

model = YOLO("yolov8n.pt")

base_dir = "C:\\Users\\Asus\\Desktop\\Foggy_Cityscapes"
no_fog_dir = os.path.join(base_dir, "No_Fog")
medium_fog_dir = os.path.join(base_dir, "Medium_Fog")
dense_fog_dir = os.path.join(base_dir, "Dense_Fog")

no_fog_images = sorted(glob(os.path.join(no_fog_dir, "*.png")))
medium_fog_images = sorted(glob(os.path.join(medium_fog_dir, "*.png")))
dense_fog_images = sorted(glob(os.path.join(dense_fog_dir, "*.png")))

iou_scores = []
count = 0
for no_fog_img, med_fog_img, dense_fog_img in zip(no_fog_images, medium_fog_images, dense_fog_images):
    count += 1
    if count == 2:
        break

    no_fog = cv2.imread(no_fog_img)
    med_fog = cv2.imread(med_fog_img)
    dense_fog = cv2.imread(dense_fog_img)
    
    enhanced_med_fog = enhance_contrast(med_fog)
    enhanced_dense_fog = enhance_contrast(dense_fog)
    
    no_fog_boxes = run_detection(model, no_fog)
    med_fog_boxes = run_detection(model, enhanced_med_fog)
    dense_fog_boxes = run_detection(model, enhanced_dense_fog)
    
    no_fog = draw_boxes(no_fog, no_fog_boxes, (0, 255, 0), "No Fog")
    med_fog = draw_boxes(med_fog, med_fog_boxes, (255, 0, 0), "Medium Fog")
    dense_fog = draw_boxes(dense_fog, dense_fog_boxes, (0, 0, 255), "Dense Fog")

    # Resize images to match height
    height = min(no_fog.shape[0], med_fog.shape[0], dense_fog.shape[0])
    no_fog = cv2.resize(no_fog, (int(no_fog.shape[1] * height / no_fog.shape[0]), height))
    med_fog = cv2.resize(med_fog, (int(med_fog.shape[1] * height / med_fog.shape[0]), height))
    dense_fog = cv2.resize(dense_fog, (int(dense_fog.shape[1] * height / dense_fog.shape[0]), height))

    # Concatenate images horizontally
    comparison = np.hstack((no_fog, med_fog, dense_fog))

    # Save the comparison image
    output_path = "comparison.jpg"
    cv2.imwrite(output_path, comparison)
    print(f"Comparison image saved as {output_path}")

    break  # Only process one image for visualization
