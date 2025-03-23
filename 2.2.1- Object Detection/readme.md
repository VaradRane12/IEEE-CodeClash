# Foggy Cityscapes Object Detection

This project evaluates object detection performance under foggy conditions using the YOLOv8 model. It compares detections in clear and foggy environments by computing Intersection over Union (IoU) scores between bounding boxes in clear and foggy images.

## Dataset

The project uses the **Foggy Cityscapes** dataset, which consists of images categorized into three levels of fog:
- **No Fog** (clear images)
- **Medium Fog**
- **Dense Fog**

Dataset structure:
```
Foggy_Cityscapes/
│── No_Fog/
│   ├── image_1.png
│   ├── image_2.png
│   └── ...
│── Medium_Fog/
│   ├── image_1.png
│   ├── image_2.png
│   └── ...
│── Dense_Fog/
│   ├── image_1.png
│   ├── image_2.png
│   └── ...
```

## Installation

Ensure you have Python installed, then install the required dependencies:

```bash
pip install -r requirements.txt
```

### `requirements.txt`
```
numpy
opencv-python
glob2
ultralytics
```

## Usage

Run the object detection script:

```bash
python detect_foggy_objects.py
```

### Functionality
- Enhances contrast using CLAHE for better visibility in foggy images.
- Runs YOLOv8 object detection on No Fog, Medium Fog, and Dense Fog images.
- Computes IoU scores between detections in clear and foggy images.
- Outputs average IoU scores for Medium and Dense fog images.

### Sample Output
```bash
Average IoU for Medium Fog: 0.5643
Average IoU for Dense Fog: 0.4231
```

## Model Used
The script uses the **YOLOv8n** model from Ultralytics. You can replace `yolov8n.pt` with other YOLOv8 models for better accuracy.

## Future Enhancements
- Support for other datasets.
- Fine-tuning YOLOv8 for better foggy environment detection.
- Additional image enhancement techniques.

## License
MIT License

