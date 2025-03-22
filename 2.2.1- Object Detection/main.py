import cv2

# Load the image
image_path = "enhanced_test.jpg"  # Your image file
image = cv2.imread(image_path)

# Load JSON data (Replace 'labels.json' with actual JSON file)
data =  {"name": "1cd5d614-35d63896.jpg",
        "attributes": {
            "weather": "rainy",
            "scene": "residential",
            "timeofday": "dawn/dusk"
        },
        "timestamp": 10000,
        "labels": [
            {
                "category": "traffic sign",
                "attributes": {
                    "occluded": False,
                    "truncated": False,
                    "trafficLightColor": "none"
                },
                "manualShape": True,
                "manualAttributes": True,
                "box2d": {
                    "x1": 815.829848,
                    "y1": 211.141262,
                    "x2": 829.572769,
                    "y2": 227.382899
                },
                "id": 311499
            },
            {
                "category": "bus",
                "attributes": {
                    "occluded": True,
                    "truncated": False,
                    "trafficLightColor": "none"
                },
                "manualShape": True,
                "manualAttributes": True,
                "box2d": {
                    "x1": 603.439229,
                    "y1": 129.933084,
                    "x2": 742.117809,
                    "y2": 284.853301
                },
                "id": 311500
            },
            {
                "category": "car",
                "attributes": {
                    "occluded": True,
                    "truncated": False,
                    "trafficLightColor": "none"
                },
                "manualShape": True,
                "manualAttributes": True,
                "box2d": {
                    "x1": 299.84558,
                    "y1": 176.159278,
                    "x2": 464.760649,
                    "y2": 323.583355
                },
                "id": 311501
            },
            {
                "category": "car",
                "attributes": {
                    "occluded": True,
                    "truncated": False,
                    "trafficLightColor": "none"
                },
                "manualShape": True,
                "manualAttributes": True,
                "box2d": {
                    "x1": 662.158988,
                    "y1": 212.390619,
                    "x2": 707.135825,
                    "y2": 298.596222
                },
                "id": 311502
            },
            {
                "category": "car",
                "attributes": {
                    "occluded": True,
                    "truncated": False,
                    "trafficLightColor": "none"
                },
                "manualShape": True,
                "manualAttributes": True,
                "box2d": {
                    "x1": 742.117809,
                    "y1": 231.130968,
                    "x2": 782.09722,
                    "y2": 274.858449
                },
                "id": 311503
            },
            {
                "category": "car",
                "attributes": {
                    "occluded": True,
                    "truncated": False,
                    "trafficLightColor": "none"
                },
                "manualShape": True,
                "manualAttributes": True,
                "box2d": {
                    "x1": 769.603654,
                    "y1": 226.13354,
                    "x2": 830.822127,
                    "y2": 284.853301
                },
                "id": 311504
            },
            {
                "category": "car",
                "attributes": {
                    "occluded": True,
                    "truncated": False,
                    "trafficLightColor": "none"
                },
                "manualShape": True,
                "manualAttributes": True,
                "box2d": {
                    "x1": 800.83757,
                    "y1": 222.38547,
                    "x2": 912.030304,
                    "y2": 304.843005
                },
                "id": 311505
            },
            {
                "category": "car",
                "attributes": {
                    "occluded": True,
                    "truncated": False,
                    "trafficLightColor": "none"
                },
                "manualShape": True,
                "manualAttributes": True,
                "box2d": {
                    "x1": 854.559902,
                    "y1": 239.876463,
                    "x2": 964.503281,
                    "y2": 329.830136
                },
                "id": 311506
            },
            {
                "category": "car",
                "attributes": {
                    "occluded": True,
                    "truncated": False,
                    "trafficLightColor": "none"
                },
                "manualShape": True,
                "manualAttributes": True,
                "box2d": {
                    "x1": 918.277087,
                    "y1": 224.884185,
                    "x2": 1180.64197,
                    "y2": 388.549897
                },
                "id": 311507
            },
            {
                "category": "car",
                "attributes": {
                    "occluded": False,
                    "truncated": True,
                    "trafficLightColor": "none"
                },
                "manualShape": True,
                "manualAttributes": True,
                "box2d": {
                    "x1": 1159.402907,
                    "y1": 292.349441,
                    "x2": 1279.356147,
                    "y2": 447.269657
                },
                "id": 311508
            },
            {
                "category": "car",
                "attributes": {
                    "occluded": False,
                    "truncated": False,
                    "trafficLightColor": "none"
                },
                "manualShape": True,
                "manualAttributes": True,
                "box2d": {
                    "x1": 346.071773,
                    "y1": 186.154131,
                    "x2": 723.377461,
                    "y2": 473.506143
                },
                "id": 311509
            },
            {
                "category": "car",
                "attributes": {
                    "occluded": False,
                    "truncated": True,
                    "trafficLightColor": "none"
                },
                "manualShape": True,
                "manualAttributes": True,
                "box2d": {
                    "x1": 0,
                    "y1": 102.44724,
                    "x2": 322.333998,
                    "y2": 483.500995
                },
                "id": 311510
            },
            {
                "category": "drivable area",
                "attributes": {
                    "areaType": "alternative"
                },
                "manualShape": True,
                "manualAttributes": True,
                "poly2d": [
                    {
                        "vertices": [
                            [
                                720.186117,
                                331.677505
                            ],
                            [
                                729.399381,
                                291.753361
                            ],
                            [
                                752.432541,
                                276.397921
                            ],
                            [
                                1280.6437,
                                491.374082
                            ],
                            [
                                1280.6437,
                                540.511491
                            ],
                            [
                                1163.958335,
                                520.549419
                            ],
                            [
                                998.119582,
                                502.12289
                            ],
                            [
                                819.774406,
                                491.615093
                            ],
                            [
                                720.186117,
                                331.677505
                            ]
                        ],
                        "types": "LLLLLCCCL",
                        "closed": True
                    }
                ],
                "id": 311511
            },
            {
                "category": "lane",
                "attributes": {
                    "laneDirection": "parallel",
                    "laneStyle": "dashed",
                    "laneType": "single white"
                },
                "manualShape": True,
                "manualAttributes": True,
                "poly2d": [
                    {
                        "vertices": [
                            [
                                817.278897,
                                494.110601
                            ],
                            [
                                729.936116,
                                353.114394
                            ]
                        ],
                        "types": "LL",
                        "closed": False
                    }
                ],
                "id": 311512
            },
            {
                "category": "lane",
                "attributes": {
                    "laneDirection": "parallel",
                    "laneStyle": "dashed",
                    "laneType": "single white"
                },
                "manualShape": True,
                "manualAttributes": True,
                "poly2d": [
                    {
                        "vertices": [
                            [
                                721.201837,
                                354.362148
                            ],
                            [
                                799.810341,
                                497.853863
                            ]
                        ],
                        "types": "LL",
                        "closed": False
                    }
                ],
                "id": 311513
            }
        ]
    }

# Extract bounding boxes
ground_values = []
for obj in data["labels"]:
    if "box2d" in obj:
        x1, y1 = int(obj["box2d"]["x1"]), int(obj["box2d"]["y1"])
        x2, y2 = int(obj["box2d"]["x2"]), int(obj["box2d"]["y2"])
        category = obj["category"]
        ground_values.append((x1,y1,x2,y2))
        # Draw the bounding box
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green box
        cv2.putText(image, category, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Show the image
print(ground_values)




from ultralytics import YOLO

model = YOLO("yolov8n.pt") 

img = cv2.imread("enhanced_test.jpg")

results = model(img)





def calculate_iou(box1, box2):
    x1, y1, x2, y2 = box1
    x1g, y1g, x2g, y2g = box2

    xi1 = max(x1, x1g)
    yi1 = max(y1, y1g)
    xi2 = min(x2, x2g)
    yi2 = min(y2, y2g)

    inter_area = max(0, xi2 - xi1) * max(0, yi2 - yi1)
    box1_area = (x2 - x1) * (y2 - y1)
    box2_area = (x2g - x1g) * (y2g - y1g)

    union_area = box1_area + box2_area - inter_area
    return inter_area / union_area if union_area else 0

# Get detected objects
detected_boxes = results[0].boxes.xyxy.cpu().numpy()

# Iterate over all detected boxes
for detected_box in detected_boxes:
    max_iou = 0  # Track the highest IoU for this detected box
    best_match = None

    # Compare with each ground truth box
    for ground_truth_box in ground_values:
        iou = calculate_iou(detected_box, ground_truth_box)
        if iou > max_iou:
            max_iou = iou
            best_match = ground_truth_box

    print(f"Detected Box: {detected_box}, Best Ground Truth Match: {best_match}, IoU: {max_iou}")


for i in results:
    i.show()
