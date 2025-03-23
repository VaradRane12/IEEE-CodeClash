import json
import os
from tqdm import tqdm

# Function to Convert COCO JSON to YOLO Format
def convert_coco_to_yolo(json_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # Load COCO JSON file
    with open(json_path, "r") as f:
        data = json.load(f)

    # Category Mapping (COCO to YOLO)
    categories = {item["id"]: item["name"] for item in data["categories"]}
    category_map = {v: i for i, v in enumerate(categories.values())}  # Convert names to YOLO class IDs

    # Process Each Image
    for image in tqdm(data["images"], desc=f"Processing {json_path}"):
        img_id = image["id"]
        img_w, img_h = image["width"], image["height"]
        label_path = os.path.join(output_dir, f"{image['file_name'].replace('.jpg', '.txt')}")

        with open(label_path, "w") as label_file:
            for ann in data["annotations"]:
                if ann["image_id"] == img_id:
                    x, y, w, h = ann["bbox"]
                    
                    # Convert to YOLO format (normalized)
                    x_center = (x + w / 2) / img_w
                    y_center = (y + h / 2) / img_h
                    w /= img_w
                    h /= img_h
                    
                    # Write to label file
                    class_id = category_map[categories[ann["category_id"]]]
                    label_file.write(f"{class_id} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}\n")

    print(f"✅ {json_path} conversion completed!")

# Convert Training Labels
convert_coco_to_yolo(
    json_path="C:/Users/Asus/Desktop/BDD100K/labels/bdd100k_labels_images_train.json",
    output_dir="C:/Users/Asus/Desktop/BDD100K/labels/yolo/train/"
)

# Convert Validation Labels
convert_coco_to_yolo(
    json_path="C:/Users/Asus/Desktop/BDD100K/labels/bdd100k_labels_images_val.json",
    output_dir="C:/Users/Asus/Desktop/BDD100K/labels/yolo/val/"
)

print("✅ All conversions completed successfully!")
