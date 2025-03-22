import cv2
import numpy as np
import torch
import joblib
import pandas as pd
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
risk_model = joblib.load("models/risk_assessment_model.pkl")

feature_columns = ["object_distance", "velocity", "trajectory_angle", "vehicle_speed"]

cap = cv2.VideoCapture("videos/input/dashcam_footage1.mp4")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

output_path = "videos/output/processed_dashcam.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

def simulate_sensor_data():
    return [
        np.random.uniform(1, 50),
        np.random.uniform(0, 20),
        np.random.uniform(-90, 90),
        np.random.uniform(10, 80)
    ]

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            label = result.names[int(box.cls[0])]

            features = simulate_sensor_data()
            features_df = pd.DataFrame([features], columns=feature_columns)
            risk_level = risk_model.predict(features_df)[0]

            color = (0, 255, 0) if risk_level == 0 else (0, 0, 255)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{label} Risk: {'High' if risk_level else 'Low'}",
                        (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    out.write(frame)
    cv2.imshow("Real-Time Risk Assessment", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Video processing complete. Saved at:", output_path)
