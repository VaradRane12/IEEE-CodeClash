import cv2
import numpy as np
from ultralytics import YOLO

def add_fog(image, intensity=0.5):
    h, w, _ = image.shape
    fog = np.full((h, w, 3), (200, 200, 200), dtype=np.uint8) 
    foggy_image = cv2.addWeighted(image, 1 - intensity, fog, intensity, 0)
    return foggy_image

image = cv2.imread("2.2.1- Object Detection\\test.jpg") 

foggy_image = add_fog(image, intensity=0.7) 
cv2.imwrite("foggy_test.jpg", foggy_image)

model = YOLO("yolov8n.pt")

results = model(foggy_image)

for result in results:
    result.show()
