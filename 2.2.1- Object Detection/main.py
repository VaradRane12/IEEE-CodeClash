from ultralytics import YOLO

import cv2

model = YOLO("yolov8n.pt") 

img = cv2.imread("foggy_test.jpg")

results = model(img)

for i in results:
    i.show()
