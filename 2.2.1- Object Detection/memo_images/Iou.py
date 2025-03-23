import cv2
import numpy as np

# Function to calculate Intersection over Union (IoU)
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

# Create a blank white image
img = np.ones((400, 400, 3), dtype=np.uint8) * 255

# Define two overlapping bounding boxes
box1 = (100, 100, 300, 300)  # (x1, y1, x2, y2)
box2 = (150, 150, 350, 350)

# Calculate IoU
iou = calculate_iou(box1, box2)

# Draw bounding boxes
cv2.rectangle(img, (box1[0], box1[1]), (box1[2], box1[3]), (255, 0, 0), 2)  # Blue box
cv2.rectangle(img, (box2[0], box2[1]), (box2[2], box2[3]), (0, 255, 0), 2)  # Green box

# Draw the intersection area
intersection_tl = (max(box1[0], box2[0]), max(box1[1], box2[1]))  # Top-left of intersection
intersection_br = (min(box1[2], box2[2]), min(box1[3], box2[3]))  # Bottom-right of intersection
cv2.rectangle(img, intersection_tl, intersection_br, (0, 0, 255), -1)  # Red filled intersection

# Put IoU text
cv2.putText(img, f'IoU: {iou:.2f}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Show image
cv2.imshow("IoU Illustration", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
